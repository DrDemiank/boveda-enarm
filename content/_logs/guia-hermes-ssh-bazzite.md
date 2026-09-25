# Guía de configuración: puente SSH Mac (Hermes) → Bazzite

Documento de instrucciones para el agente de IA que asista en la configuración.
Ejecutar en orden. No omitir las verificaciones.

---

## 1. Contexto y objetivo

**Situación actual**

- El agente Hermes ("La Mole") corre en una **Mac Intel con macOS Monterey**.
- La estación de trabajo principal es un **PC con Bazzite Linux** (Ryzen 7 7700X, Radeon RX 9070 XT 16 GB, 32 GB DDR5).
- Ya existe un puente en sentido **Bazzite → Mac** (script `hermes_voz.py`, sesión SSH persistente `jarvis_voz`, sin contraseña).
- Falta el sentido inverso.

**Objetivo**

Habilitar el sentido **Mac → Bazzite** para que Hermes, corriendo en la Mac, delegue en el PC Bazzite todo trabajo que requiera GPU, CPU multinúcleo o volumen de disco: fotogrametría, transcodificación de video, inferencia local con Ollama, compilaciones y procesamiento de imágenes.

**Justificación**

La Mac Intel no tiene capacidad de cómputo para estas cargas. El agente debe conservar su razonamiento en la Mac y usar Bazzite exclusivamente como nodo de ejecución.

**Restricción de arquitectura**

Bazzite es un sistema inmutable basado en Fedora Atomic. No se instala software con `dnf` en el sistema base. Todo el software de trabajo vive dentro de contenedores **Distrobox**. Toda ejecución remota debe envolverse en `distrobox enter <contenedor> -- bash -lc '<comando>'`.

---

## 2. Variables a definir antes de empezar

Sustituir en todos los comandos posteriores:

| Variable | Descripción | Cómo obtenerla |
|---|---|---|
| `USUARIO` | Usuario de Linux en Bazzite | En Bazzite: `whoami` |
| `HOST_BAZZITE` | Nombre mDNS o IP fija del PC | En Bazzite: `hostname` y `ip -4 addr` |
| `CONTENEDOR` | Nombre del Distrobox de trabajo | En Bazzite: `distrobox list` |

Se recomienda `HOST_BAZZITE = <hostname>.local` si la red resuelve mDNS. Si no resuelve, usar la IP y **reservarla en el router por MAC**, para que no cambie con DHCP.

---

## 3. Preparación del lado Bazzite

Ejecutar en la terminal del PC Bazzite.

### 3.1 Levantar el servidor SSH

```
sudo systemctl enable --now sshd
systemctl status sshd --no-pager
```

Debe reportar `active (running)`.

### 3.2 Abrir el puerto en el cortafuegos

```
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
sudo firewall-cmd --list-services
```

Debe aparecer `ssh` en la lista.

### 3.3 Obtener los datos de conexión

```
whoami
hostname
ip -4 addr show | grep inet
```

Anotar usuario, hostname e IP de la interfaz activa.

### 3.4 Verificar resolución mDNS (opcional pero recomendable)

```
systemctl status avahi-daemon --no-pager
```

Si está activo, el equipo será alcanzable como `<hostname>.local`.

### 3.5 Confirmar el contenedor de trabajo

```
distrobox list
```

Si no existe un contenedor para tareas pesadas, crearlo:

```
distrobox create --name foto --image ubuntu:24.04
distrobox enter foto -- bash -lc 'sudo apt update && sudo apt install -y build-essential rsync tmux'
```

### 3.6 Confirmar que `tmux` existe en el sistema base

```
which tmux || rpm-ostree install tmux
```

`tmux` es necesario en el **host**, no solo dentro del contenedor, para que los procesos largos sobrevivan al cierre de la sesión SSH. Si se instala con `rpm-ostree`, requiere reinicio.

---

## 4. Preparación del lado Mac

Ejecutar en la terminal de la Mac.

### 4.1 Generar una llave dedicada al agente

No reutilizar la llave personal. El agente debe tener una llave propia, revocable de forma independiente.

```
ssh-keygen -t ed25519 -f ~/.ssh/id_hermes_bazzite -C "hermes-agente-bazzite"
```

Dejar la frase de paso **vacía**: un agente no interactivo no puede escribirla.

### 4.2 Copiar la llave pública a Bazzite

```
ssh-copy-id -i ~/.ssh/id_hermes_bazzite.pub USUARIO@HOST_BAZZITE
```

Si `ssh-copy-id` no está disponible:

```
cat ~/.ssh/id_hermes_bazzite.pub | ssh USUARIO@HOST_BAZZITE "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

### 4.3 Crear el alias de conexión

Editar `~/.ssh/config` en la Mac y añadir:

```
Host bazzite
    HostName HOST_BAZZITE
    User USUARIO
    IdentityFile ~/.ssh/id_hermes_bazzite
    IdentitiesOnly yes
    ServerAliveInterval 30
    ServerAliveCountMax 6
    ControlMaster auto
    ControlPath ~/.ssh/cm-%r@%h:%p
    ControlPersist 10m
```

Ajustar permisos:

```
chmod 600 ~/.ssh/config
```

`ControlMaster` y `ControlPersist` mantienen abierto un canal multiplexado durante diez minutos. Esto evita renegociar la conexión en cada llamada del agente y reduce de forma notable la latencia cuando encadena varios comandos.

### 4.4 Verificar

```
ssh bazzite 'uname -a; nproc; free -h; df -h ~'
```

Debe responder sin solicitar contraseña.

---

## 5. Patrones de ejecución que el agente debe usar

### 5.1 Comando simple en el host

```
ssh bazzite 'ls -la ~/biblioteca'
```

### 5.2 Comando dentro del contenedor Distrobox

`distrobox enter` sin argumentos abre una sesión interactiva y **falla** por SSH no interactivo. Siempre usar la forma con `--`:

```
ssh bazzite "distrobox enter CONTENEDOR -- bash -lc 'colmap --help'"
```

Atención al anidamiento de comillas: dobles hacia fuera, simples hacia dentro. Si el comando interno requiere comillas dobles, escaparlas con `\"`.

### 5.3 Proceso largo que debe sobrevivir a la sesión

Nunca lanzar un proceso de horas en primer plano por SSH. Usar `tmux` con sesión con nombre y volcado a bitácora:

```
ssh bazzite "tmux new-session -d -s TRABAJO 'distrobox enter CONTENEDOR -- bash -lc \"cd ~/biblioteca && <COMANDO_LARGO>\" > ~/biblioteca/TRABAJO.log 2>&1'"
```

### 5.4 Consultar avance

```
ssh bazzite "tmux list-sessions"
ssh bazzite "tail -n 40 ~/biblioteca/TRABAJO.log"
```

### 5.5 Verificar si el trabajo terminó

```
ssh bazzite "tmux has-session -t TRABAJO 2>/dev/null && echo EN_CURSO || echo TERMINADO"
```

### 5.6 Transferencia de archivos

Subir insumos:

```
rsync -avP ~/fotos_biblioteca/ bazzite:~/biblioteca/images/
```

Descargar resultados:

```
rsync -avP bazzite:~/biblioteca/salida/ ~/resultados/
```

`rsync` es preferible a `scp` porque reanuda transferencias interrumpidas y no reenvía lo ya copiado.

---

## 6. Reglas de seguridad de obligado cumplimiento

Estas reglas deben quedar escritas también en la skill del agente.

1. La llave `id_hermes_bazzite` es exclusiva para este puente. No copiarla a otros equipos ni reutilizarla para otros servicios.
2. El agente **no ejecuta** `rm -rf`, `dd`, `mkfs`, `rpm-ostree`, `shutdown`, `reboot` ni ningún `sudo` de forma autónoma. Si una tarea los requiere, imprime el comando y solicita autorización explícita al usuario.
3. El agente **no modifica** archivos fuera del directorio de trabajo acordado para cada proyecto.
4. Antes de cualquier operación destructiva o de sobrescritura, listar primero lo que se va a afectar y confirmar.
5. No exponer el puerto 22 a Internet. Este puente opera solo dentro de la red local.
6. Para revocar el acceso del agente basta con eliminar su línea de `~/.ssh/authorized_keys` en Bazzite.

---

## 7. Diagnóstico de fallos frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| `Could not resolve hostname` | mDNS no resuelve en la red | Usar la IP directa y reservarla en el router |
| `Connection refused` | `sshd` apagado o puerto cerrado | Revisar los pasos 3.1 y 3.2 |
| Sigue pidiendo contraseña | Permisos incorrectos en Bazzite | `chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys` |
| `Permission denied (publickey)` | Llave equivocada | Diagnosticar con `ssh -v bazzite` y revisar `IdentityFile` |
| `distrobox: command not found` | Shell no interactiva sin PATH completo | Usar `bash -lc` como en 5.2 |
| El proceso muere al terminar el comando | Se lanzó en primer plano | Relanzar con `tmux` según 5.3 |
| La IP cambió | DHCP sin reserva | Reserva por MAC en el router o IP estática |
| Latencia alta entre comandos | Multiplexación inactiva | Verificar `ControlPath` y permisos de `~/.ssh/config` |

---

## 8. Lista de comprobación final

- [ ] `sshd` activo y habilitado al arranque en Bazzite
- [ ] Puerto 22 abierto en `firewalld`
- [ ] Llave `id_hermes_bazzite` generada sin frase de paso
- [ ] Llave pública instalada en `authorized_keys` de Bazzite
- [ ] Bloque `Host bazzite` presente en `~/.ssh/config` de la Mac
- [ ] `ssh bazzite 'uname -a'` responde sin contraseña
- [ ] `tmux` disponible en el host Bazzite
- [ ] Contenedor Distrobox de trabajo creado y accesible por SSH
- [ ] `rsync` funcional en ambos sentidos
- [ ] Skill de ejecución remota instalada en `~/.hermes/skills/`
