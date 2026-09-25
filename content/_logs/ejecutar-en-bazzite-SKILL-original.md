---
name: ejecutar-en-bazzite
description: Delega cómputo pesado desde la Mac al PC Bazzite por SSH. Se activa ante fotogrametría, transcodificación de video, inferencia con GPU, compilación de código, procesamiento por lotes de imágenes o cualquier tarea que exceda la capacidad de la Mac Intel.
version: 1
---

# Ejecución remota en Bazzite

## 1. Propósito

Esta skill me permite usar el PC Bazzite como nodo de cómputo. Yo razono y decido en la Mac; Bazzite ejecuta.

Hardware disponible en el nodo remoto: Ryzen 7 7700X, Radeon RX 9070 XT de 16 GB, 32 GB DDR5.

## 2. Cuándo activarla

Activo esta skill cuando la tarea implique cualquiera de lo siguiente:

- Fotogrametría, reconstrucción 3D, nubes de puntos o mallas
- Transcodificación, extracción de cuadros o filtrado de video
- Inferencia con GPU, Ollama, modelos de difusión
- Compilación desde fuente
- Procesamiento por lotes de más de cincuenta imágenes
- Cualquier proceso con duración estimada superior a diez minutos
- Cualquier tarea que requiera más de 8 GB de RAM

No la activo para: edición de texto, redacción, búsqueda web, generación de documentos, ni operaciones de archivo pequeñas. Esas las resuelvo localmente en la Mac.

## 3. Restricción de arquitectura

Bazzite es un sistema **inmutable** basado en Fedora Atomic. El software de trabajo no vive en el sistema base, sino dentro de contenedores **Distrobox**.

Consecuencia operativa: casi todo comando de trabajo debe envolverse así:

```
ssh bazzite "distrobox enter CONTENEDOR -- bash -lc 'COMANDO'"
```

`distrobox enter` sin `--` abre una sesión interactiva y falla por SSH. La forma con `--` y `bash -lc` es obligatoria.

## 4. Protocolo de arranque

Antes de la primera ejecución de cada sesión de trabajo, verifico el estado del nodo:

```
ssh bazzite 'uname -a; nproc; free -h; df -h ~'
```

```
ssh bazzite 'distrobox list'
```

Si la conexión falla, no improviso: reporto el error exacto al usuario y consulto la guía `guia-hermes-ssh-bazzite.md`, sección 7.

## 5. Patrones de ejecución

### 5.1 Comando corto en el host

```
ssh bazzite 'ls -la ~/RUTA'
```

### 5.2 Comando corto dentro del contenedor

```
ssh bazzite "distrobox enter CONTENEDOR -- bash -lc 'VERSION_O_AYUDA'"
```

### 5.3 Trabajo largo (obligatorio con tmux)

Nunca lanzo un proceso de larga duración en primer plano. Se perdería al cerrarse la sesión SSH.

```
ssh bazzite "tmux new-session -d -s NOMBRE_TRABAJO 'distrobox enter CONTENEDOR -- bash -lc \"cd ~/PROYECTO && COMANDO_LARGO\" > ~/PROYECTO/NOMBRE_TRABAJO.log 2>&1'"
```

Reglas para el nombre de sesión: minúsculas, sin espacios, descriptivo del proyecto.

### 5.4 Seguimiento

```
ssh bazzite "tmux list-sessions"
ssh bazzite "tail -n 40 ~/PROYECTO/NOMBRE_TRABAJO.log"
ssh bazzite "tmux has-session -t NOMBRE_TRABAJO 2>/dev/null && echo EN_CURSO || echo TERMINADO"
```

Consulto el avance a intervalos razonables. No hago sondeo en bucle cerrado ni encadeno decenas de llamadas seguidas.

### 5.5 Cancelación

```
ssh bazzite "tmux kill-session -t NOMBRE_TRABAJO"
```

Solo cancelo cuando el usuario lo pide o cuando la bitácora muestra un error irrecuperable, y en ese segundo caso lo informo antes.

### 5.6 Transferencia de archivos

Subida de insumos:

```
rsync -avP ~/ORIGEN/ bazzite:~/PROYECTO/DESTINO/
```

Descarga de resultados:

```
rsync -avP bazzite:~/PROYECTO/salida/ ~/resultados/
```

Uso `rsync` y no `scp`: reanuda transferencias y no reenvía lo ya copiado.

### 5.7 Sintaxis de comillas

Orden de anidamiento: comilla doble hacia fuera, comilla simple hacia dentro, comilla doble escapada (`\"`) en el nivel más profundo. Antes de enviar un comando con tres niveles, lo reviso carácter por carácter. Un error de comillas aquí produce fallos silenciosos difíciles de diagnosticar.

## 6. Prohibiciones absolutas

No ejecuto de forma autónoma, bajo ninguna circunstancia:

- `rm -rf`, `rm` recursivo, o borrado de cualquier directorio
- `dd`, `mkfs`, `fdisk`, `parted`
- `rpm-ostree` en cualquiera de sus formas
- `shutdown`, `reboot`, `systemctl disable`
- Cualquier comando con `sudo`
- Modificación de `~/.ssh/`, `/etc/`, o archivos de configuración del sistema
- Escritura fuera del directorio de proyecto acordado

Si la tarea requiere alguno de estos, **imprimo el comando en texto plano y solicito autorización explícita al usuario**. No lo ejecuto yo.

Antes de sobrescribir cualquier archivo existente, listo primero lo que se va a afectar y pido confirmación.

## 7. Manejo de errores

Ante un fallo, sigo esta secuencia:

1. Capturo la salida de error completa, sin resumirla ni interpretarla todavía.
2. Consulto la tabla de diagnóstico de `guia-hermes-ssh-bazzite.md`, sección 7.
3. Si el fallo es de conexión, diagnostico con `ssh -v bazzite` y reporto.
4. Si el fallo es del programa remoto, reviso la bitácora completa antes de proponer una corrección.
5. Máximo dos intentos de corrección automática. Al tercer fallo, me detengo y presento al usuario el error, lo que intenté y qué hipótesis tengo.

No invento la causa de un error. Si la salida no la explica, lo digo.

## 8. Informe al usuario

Al lanzar un trabajo, reporto: nombre de sesión tmux, ruta de la bitácora y estimación de duración si la tengo.

Al terminar, reporto: estado final, ruta de los resultados en Bazzite, tamaño de la salida y si ya se descargaron a la Mac.

Uso trato de usted, tono formal y neutro, sin emojis. Los comandos siempre en texto plano dentro de bloques de código, para que el usuario pueda copiarlos y verificarlos por su cuenta.

## 9. Referencia cruzada

Configuración completa del puente, variables de conexión y lista de comprobación: `guia-hermes-ssh-bazzite.md`.
