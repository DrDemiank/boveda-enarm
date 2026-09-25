# Plan: modelo local pequeño en Bazzite coordinado con Hermes

Documento de trabajo para Hermes (La Mole y equipo) y para Demian (Mr. Fantástico), quien dirige, aporta ejemplos reales y valida resultados.

Versión 1.0 — septiembre 2026

---

## 1. Objetivo

Contar con un modelo de lenguaje pequeño (3–4B parámetros), alojado en el equipo Bazzite y ajustado con Unsloth, que ejecute de forma local, rápida y privada tareas repetitivas de transformación de texto. El modelo NO se usa como fuente de conocimiento: solo trabaja con el material que Demian proporciona (PDFs, notas, censos, bóveda de Obsidian).

Las tareas pesadas, de razonamiento o de edición compleja se escalan a modelos grandes (Ollama Cloud: GLM / Kimi / DeepSeek) o a Claude.

### Tareas objetivo

| Tarea | Quién hace qué |
|---|---|
| Transcribir PDFs | Herramienta de OCR/extracción obtiene el texto; el modelo pequeño lo limpia y ordena |
| Acomodar notas clínicas | Modelo pequeño con ajuste fino (formato institucional) |
| Registrar censos | Modelo pequeño extrae datos a JSON; un script en Python valida y escribe en el Excel |
| Mejorar prompts (paso inicial) | Modelo pequeño convierte una petición breve en prompt estructurado para modelos grandes |
| Consultar Obsidian | Búsqueda (RAG) recupera notas; el modelo pequeño redacta solo con lo recuperado |

### Principio rector

El modelo pequeño se encarga del paso lingüístico. Todo lo que deba ser exacto (escribir en Excel, fechas, conteos, validaciones) lo hace código.

---

## 2. Arquitectura

```
                 ┌──────────────────────────────┐
  Demian ──────► │  Hermes (Mac, orquestador)   │
                 └──────────────┬───────────────┘
                                │ decide la ruta
          ┌─────────────────────┼──────────────────────┐
          ▼                     ▼                      ▼
 ┌─────────────────┐  ┌───────────────────┐  ┌──────────────────┐
 │ Modelo pequeño  │  │ Ollama Cloud      │  │ Claude           │
 │ Bazzite (GPU)   │  │ GLM / Kimi / DS   │  │ trabajos         │
 │ vía red local   │  │ tareas medias     │  │ importantes      │
 └────────┬────────┘  └───────────────────┘  └──────────────────┘
          │
   ┌──────┴───────────────────────────┐
   │ Herramientas locales en Bazzite  │
   │ - OCR / extracción de PDF        │
   │ - Script de censo (openpyxl)     │
   │ - Índice RAG de Obsidian         │
   └──────────────────────────────────┘
```

- Equipo de entrenamiento y servicio: Bazzite (Ryzen 7 7700X, RX 9070 XT 16 GB, 32 GB DDR5).
- Orquestador: Hermes en la Mac, que consulta al modelo pequeño por la red local.
- Condición: la PC Bazzite debe estar encendida. Si no responde, Hermes enruta la tarea a Ollama Cloud.

### Reglas de escalamiento (para Hermes)

Enviar al modelo pequeño cuando:
- La tarea es de formato, limpieza, extracción o reordenamiento de texto ya existente.
- La entrada cabe en el contexto del modelo (fijar límite práctico, p. ej. ~6 000 tokens).

Escalar a Ollama Cloud cuando:
- Se requiere búsqueda en internet, investigación o síntesis de varias fuentes.
- El modelo pequeño devuelve JSON inválido dos veces seguidas o falla la validación.
- El texto de entrada excede el límite de contexto.

Escalar a Claude cuando:
- Es un entregable importante (certificación MOCEBPASS, trabajos doctorales, documentos oficiales complejos).
- Hay edición compleja de documentos (.docx estructurados, verificación con referencias).
- Demian lo indica expresamente.

---

## 3. Fases del proyecto

### Fase 0 — Preparar el entorno en Bazzite

Bazzite es inmutable; el entrenamiento se hace dentro de una Distrobox con acceso a la GPU.

1. Verificar que el sistema ve la GPU:

```
rocminfo | grep -i gfx
```

Debe aparecer `gfx1201`.

2. Crear el contenedor a partir de la imagen oficial de ROCm con PyTorch:

```
distrobox create --name unsloth --image docker.io/rocm/pytorch:latest --additional-flags "--device /dev/kfd --device /dev/dri --group-add video --group-add render"
distrobox enter unsloth
```

3. Comprobar que PyTorch detecta la GPU dentro del contenedor:

```
python3 -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
```

Debe imprimir `True` y el nombre de la Radeon.

4. Instalar Unsloth siguiendo la guía oficial para AMD (https://unsloth.ai/docs/get-started/install/amd). La guía indica cómo elegir la rueda de PyTorch según la versión de ROCm; no instalar versiones al azar. Alternativa sin terminal: Unsloth Studio para Linux, que detecta la GPU AMD automáticamente.

Criterio de salida de la fase: un cuaderno de ejemplo de Unsloth con un modelo de 1–4B entrena algunos pasos sin error.

---

### Fase 1 — Línea base SIN entrenamiento

Antes de entrenar, medir qué tan bien lo hace un modelo pequeño con buenas instrucciones. Muchas tareas podrían no necesitar ajuste fino.

1. Descargar en Ollama (Bazzite) un modelo instruct de 3–4B con buen desempeño en español (familia Qwen como primera opción).
2. Escribir un system prompt por tarea (notas, censo, prompts).
3. Probar con 20 ejemplos reales anonimizados por tarea.
4. Registrar resultados en una tabla: correcto / error menor / error grave.

Decisión:
- Si una tarea supera ~90 % de resultados correctos, se queda con prompt y no se entrena.
- Si no, pasa a la Fase 2.

Expectativa: notas clínicas probablemente requieran entrenamiento; mejora de prompts y consulta de Obsidian probablemente no.

---

### Fase 2 — Construir el conjunto de datos

Es la fase que más determina la calidad final.

#### Formato

Un archivo JSONL por tarea, formato conversacional:

```
{"messages": [{"role": "system", "content": "Eres un asistente que reordena notas clínicas al formato institucional del HSMO."}, {"role": "user", "content": "<nota desordenada>"}, {"role": "assistant", "content": "<nota final correcta>"}]}
```

#### Cantidad orientativa

- 200–500 ejemplos de buena calidad por tarea.
- Separar 10–15 % como conjunto de prueba que el modelo nunca ve durante el entrenamiento.

#### Origen de los ejemplos

1. Demian aporta ejemplos reales: entrada original y versión final que él considera correcta.
2. Hermes genera variaciones (distinto orden, abreviaturas, errores de captura, datos faltantes) a partir de esos ejemplos.
3. Demian revisa una muestra de las variaciones antes de incluirlas.

#### Reglas obligatorias de privacidad

- Anonimizar TODO dato de paciente antes de que entre al conjunto: nombres, expedientes, CURP, fechas de nacimiento exactas, domicilios, teléfonos, nombres de familiares.
- Sustituir por datos ficticios consistentes (no dejar huecos, para que el modelo aprenda la estructura).
- Los archivos del conjunto de datos no salen de Bazzite ni se suben a servicios en la nube.
- El modelo puede memorizar fragmentos; por eso la anonimización es previa, no posterior.

#### Nota sobre términos de uso

Si se usan salidas de servicios comerciales (Claude, Ollama Cloud u otros) para generar ejemplos de entrenamiento, revisar antes los términos de uso de cada proveedor sobre ese uso.

#### Particularidades por tarea

- Censo: la salida del modelo es SOLO JSON con un esquema fijo (ver Fase 5). Los ejemplos deben incluir casos con campos faltantes marcados como `null`, nunca inventados.
- Prompts: incluir ejemplos donde falta información y el modelo lo señala con una sección "Datos faltantes" en lugar de rellenar.
- Notas: incluir la plantilla institucional completa en los ejemplos para fijar el orden de apartados.

---

### Fase 3 — Entrenamiento con Unsloth (QLoRA)

Parámetros iniciales razonables para 3–4B en 16 GB de VRAM (ajustar según resultados):

| Parámetro | Valor inicial |
|---|---|
| Método | QLoRA (carga en 4 bits) |
| Rango LoRA (r) | 16 |
| lora_alpha | 16 |
| Tasa de aprendizaje | 2e-4 |
| Épocas | 2–3 |
| Longitud máxima de secuencia | 4096 (notas) / 2048 (censo, prompts) |
| Entrenar solo en respuestas | Sí (enmascarar el texto del usuario) |

Recomendación: entrenar un adaptador LoRA por tarea en lugar de uno solo para todo, al menos al inicio. Es más fácil de evaluar y corregir.

Señales de alerta:
- Pérdida de validación que sube mientras la de entrenamiento baja: sobreajuste; reducir épocas.
- El modelo repite frases de ejemplos: poca variedad en los datos.

Exportación:
- Exportar a GGUF con cuantización q4_k_m (o q8_0 si la calidad lo requiere y la VRAM lo permite).

---

### Fase 4 — Servir el modelo en Bazzite y conectarlo con Hermes

1. Crear un Modelfile para Ollama:

```
FROM ./hsmo-notas-q4_k_m.gguf
PARAMETER temperature 0.2
SYSTEM "Eres un asistente que reordena notas clínicas al formato institucional del HSMO. No agregues información que no esté en la entrada."
```

2. Registrar el modelo:

```
ollama create hsmo-notas -f Modelfile
```

3. Permitir que Ollama escuche en la red local (servicio de usuario systemd existente):

```
systemctl --user edit ollama
```

Agregar:

```
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
```

Luego:

```
systemctl --user daemon-reload
systemctl --user restart ollama
```

4. Abrir el puerto solo para la red local (firewalld en Bazzite). No exponer el puerto a internet.

5. Desde la Mac, comprobar conexión:

```
curl http://IP_DE_BAZZITE:11434/api/tags
```

6. En Hermes, agregar un proveedor compatible con OpenAI apuntando a:

```
http://IP_DE_BAZZITE:11434/v1
```

Asignar una IP fija a Bazzite en el router para que la dirección no cambie.

---

### Fase 5 — Herramientas de apoyo por tarea

#### Transcripción de PDFs

- PDF con texto seleccionable: extracción directa sin IA (pdftotext o PyMuPDF).
- PDF escaneado o fotos: OCR (Docling, Marker o Tesseract) o un modelo pequeño de visión en Bazzite.
- Después: el modelo pequeño limpia saltos de línea, encabezados repetidos y ordena el texto.

#### Censo diario

Flujo:

1. Demian pega o dicta los datos del día.
2. El modelo pequeño devuelve JSON con esquema fijo, por ejemplo:

```
{"fecha": "2026-09-15", "servicio": "hombres", "pacientes": [{"cama": "", "nombre": "", "edad": null, "fecha_ingreso": "", "diagnostico": "", "observaciones": ""}]}
```

3. Script en Python (openpyxl) que:
   - Valida el JSON contra el esquema.
   - Rechaza campos obligatorios vacíos y fechas incongruentes.
   - Aplica los criterios fijos de armado del censo.
   - Escribe en la hoja correspondiente a la fecha.
   - Muestra un resumen de cambios para que Demian confirme antes de guardar.

El modelo nunca escribe directamente en el Excel.

#### Mejora de prompts

Plantilla de salida fija:

```
## Rol
## Contexto
## Tarea
## Formato de salida
## Restricciones
## Datos faltantes (preguntar a Demian)
```

#### Consulta de la bóveda de Obsidian

- Indexar las notas .md con un modelo de embeddings local vía Ollama (p. ej. nomic-embed-text o bge-m3).
- Almacén vectorial local (Chroma o LanceDB).
- El modelo pequeño responde solo con los fragmentos recuperados y cita el nombre de la nota de origen.
- Si no encuentra información, debe decirlo; no completar de memoria.
- Integrar con la skill existente `second-brain` de La Mole en lugar de duplicarla.

---

### Fase 6 — Evaluación continua

Usar el conjunto de prueba separado en la Fase 2.

| Tarea | Métrica |
|---|---|
| Notas | Estructura correcta; cero datos agregados que no estaban en la entrada |
| Censo | JSON válido; exactitud de campos al 100 % contra revisión manual |
| Prompts | Demian califica 1–5 si el prompt resultante sirvió sin retoques |
| Obsidian | Respuesta sustentada en la nota citada; sin información inventada |
| PDFs | Comparación del texto limpio contra el original en una muestra |

Regla de seguridad clínica: toda salida que vaya a un documento oficial o expediente es revisada por Demian antes de usarse. El modelo es una herramienta de apoyo, no sustituye la revisión médica.

---

## 4. Reparto de trabajo sugerido (esquema de los Cuatro Fantásticos)

| Integrante | Responsabilidad |
|---|---|
| Mr. Fantástico (Demian) | Define prioridades, aporta ejemplos reales anonimizados, valida muestras y resultados, aprueba cada fase |
| La Mole | Scripts de entrenamiento, generación de variaciones del conjunto de datos, script de censo, integración con Hermes |
| La Antorcha Humana | Evaluación: corre el conjunto de prueba, llena tablas de resultados, detecta errores recurrentes |
| La Mujer Invisible | Tareas ligeras: plantillas de prompts, documentación de cada fase, bitácora de cambios |
| Claude | Revisión de diseño, depuración compleja, decisiones de arquitectura y entregables importantes |

---

## 5. Orden recomendado de implementación

1. Fase 0 completa (entorno funcionando).
2. Censo: línea base con prompt + script de validación. Es la tarea más repetitiva y la más fácil de medir.
3. Notas clínicas: conjunto de datos y primer ajuste fino.
4. Conexión Bazzite–Hermes por red local y reglas de escalamiento.
5. Transcripción de PDFs (OCR + limpieza).
6. Mejora de prompts.
7. RAG de Obsidian.

---

## 6. Bitácora de decisiones

| Fecha | Decisión | Motivo |
|---|---|---|
| 2026-09-15 | Alojar y entrenar el modelo en Bazzite, no en la Mac | La Mac Intel con Monterey no tiene aceleración por GPU ni soporte oficial de Ollama actual |
| 2026-09-15 | El modelo pequeño no será fuente de conocimiento | Solo transforma material propio; lo exacto lo hace código |
| | | |


## 7. VEREDICTO TÉCNICO (15/09/2026) — investigación La Mole

VIABLE con 2 correcciones obligatorias y 1 limitante gestionable:

1. IMAGEN CORREGIDA: NO usar distrobox + rocm/pytorch:latest (estático desde
   ago/2026, sin ROCm 7.x). Opción A: Docker/podman con unsloth/unsloth-rocm:latest
   (oficial Unsloth, push 15-sep-2026, RDNA4 gfx1201 declarado, preinstala
   PyTorch+bitsandbytes+llama.cpp ROCm). Opción B (verificada en RX 9070 XT real):
   rocm/dev-ubuntu-24.04:7.2.4-complete + curl -fsSL https://unsloth.ai/install.sh | sh
2. bitsandbytes OBLIGATORIO pre-release 1.33.7.preview (versiones ≤0.49.2
   tienen bug NaN en 4-bit en TODAS las GPU AMD) — paso que faltaba en el plan
   y causa típica de NaN en loss.
3. QLoRA 4-bit en RDNA4: INESTABLE reportado (log real usó 8-bit). Mitigación:
   empezar 4-bit; si hay NaN/OOM, caer a 8-bit (cabe: ~8-10 GB de los 15.9).
4. MODELO BASE: Qwen3-4B-Instruct-2507 (ollama library: qwen3:4b-instruct-2507-q4_K_M).
   No-thinking (mejor para asistente clínico). Alternativa: gemma-3-4b-it.
   AVISO: NO usar Qwen3.5 para QLoRA (aviso oficial Unsloth 13-ago-2026).
5. VRAM/TIEMPO: 4B a 8-bit cabe holgado (~8-10 GB de 15.9). Tiempo estimado
   (derivado de log real RDNA4: 5.28 s/it): 300 ej × 3 ép ≈ 4 h; rango del
   plan 200-500 ej × 2-3 ép ≈ 3-8 h. No garantizado.
6. Exportación GGUF→Ollama: pipeline oficial funcional en AMD (llama.cpp
   ROCm prebuilt matched a gfx1201 dentro del contenedor).
7. Variables del script: HF_HUB_DISABLE_XET=1; ROCR_VISIBLE_DEVICES="0"
   (la iGPU Raphael aparece como 2do dispositivo); average_tokens_across_devices=False.
   FlashAttention 2 no existe en ROCm (cae a Xformers, warning inofensivo).

### FASE 0 CORREGIDA (sustituye la del plan):
docker pull unsloth/unsloth-rocm:latest
docker run --rm -it --device /dev/kfd --device /dev/dri \
  --group-add video --group-add render --ipc=host \
  --security-opt seccomp=unconfined -v /var/home/Demiank/unsloth:/workspace \
  unsloth/unsloth-rocm:latest
Verificación dentro: amd-smi version && python3 -c "import torch; print(torch.cuda.is_available())"

### Bitácora añadida:
| 2026-09-15 | Imagen unsloth/unsloth-rocm en vez de rocm/pytorch:latest | la última quedó estática sin ROCm 7.x; la oficial Unsloth declara RDNA4 |
| 2026-09-15 | bitsandbytes 1.33.7.preview obligatorio | versiones viejas causan NaN en 4-bit en GPU AMD |
| 2026-09-15 | QLoRA empezar 4-bit, caer a 8-bit si NaN | reporte real de RDNA4 usó 8-bit por inestabilidad |


## 8. Comparativa familia MiniCPM (15/09/2026) — pregunta del doctor

Variantes investigadas: MiniCPM-V 2.6 (8B visión, vieja), MiniCPM-V 4.5 (8B
visión, empate técnico con qwen3-vl), MiniCPM-V 4.6 (1.6GB, Qwen3.5-0.8B),
MiniCPM5-2B (2.5B TEXTO nuevo sept-2026, 131K ctx, Apache 2.0, agéntico,
supera Qwen3.5-4B según ficha de ModelBest — no reproducido externamente).

VEREDICTO para editar egresos/notas:
- MiniCPM5-2B: NO para redacción clínica (2.5B agéntico, poco vocabulario
  médico; solo build de comunidad en Ollama, no library oficial)
- MiniCPM-V 2.6/4.5/4.6: modelos de VISIÓN (leen documentos) — su rol sería
  LEER expedientes, no EDITAR texto
- MiniCPM-V 4.5/4.6 como SEGUNDO lector de expedientes: experimento válido
  (doble lectura OCR reduce riesgo de dosis mal leídas)
- Devlog feb-2026 (Qwen3-VL vs MiniCPM-V en 8GB): MiniCPM-V fabricó un KDA
  y matcheó commits equivocados; Qwen3-VL ganó por OCR estable y baja
  alucinación → qwen3-vl:8b sigue siendo los ojos del flujo
- Para EDITAR texto clínico: qwen3:14b (instalado, probado) y el futuro
  qwen3:4b fine-tuned HSMO siguen siendo la vía correcta


## 9. Comparativa EN VIVO qwen3.5:4b vs qwen3:14b (16/09/2026, RX 9070 XT)

Stack verificado tras encendido: Ollama ROCm v7.2, GPU RX 9070 XT 15.9 GiB
detectada, 0.0.0.0:11434 accesible desde la Mac ✓ (firewall OK), context
32768, flash attention, KV q8_0. Modelos: gpt-oss:20b, qwen3:14b,
qwen3-vl:8b, glm-ocr:q8_0, bge-m3 + qwen3.5:4b (nuevo, 3.4 GB descargado
en vivo a 56 MB/s).

Prueba: mismo system prompt (egreso HSMO, anti-invención) + mismo JSON
de prueba (esquizofrenia paranoide F20.0, olanzapina 10 mg):

- qwen3.5:4b — 36.8 s, 2440 tokens: texto correcto y fiel a los datos,
  pero organiza las secciones con errores estructurales (estado al egreso
  y pronóstico dentro de "Recomendaciones", plan casi vacío con solo el
  esquema del fármaco). Verboso (thinking largo).
- qwen3:14b — 24.4 s, 670 tokens: estructura PERFECTA (resumen con CIE-10,
  plan narrativo, recomendaciones numeradas), redacción clínica natural,
  más rápido. VEREDICTO: mejor para edición de egresos.

Decisión: qwen3:14b queda como el editor de egresos en la línea base.
qwen3.5:4b se queda instalado (3.4 GB) para el fine-tuning experimental
(SOLO con 8-bit según aviso Unsloth — no QLoRA 4-bit en Qwen3.5).


## 10. Dataset construido y entrenamiento lanzado (2026-09-16)

- Descarga Drive verificada: 343/343 (94 MB), sin anonimizar (decisión del
  doctor — todo permanece local)
- Extracción: 20 egresos + 318 notas (1.23 MB de texto), 0 errores
- Clasificación: 87 evolución, 14 consulta externa, 5 valoración, 1
  urgencias, 153 indicaciones (36 pares nota→INDICAS detectados)
- DATASET FINAL: 161 pares = 139 train + 22 test (15% estratificado)
  - train: 17 egresos, 91 evoluciones, 31 indicaciones
  - median 1,295 tokens, max ~13k → seq_max 8192 (conserva todos)
- Script finetune_hsmo.py subido a Bazzite:~/unsloth/ junto con los datasets
- QLoRA 8-bit (no 4-bit, riesgo RDNA4), r=16, 3 épocas, lr 2e-4,
  qwen3:4b-instruct-2507, bf16, adamw_8bit
- PULL de unsloth/unsloth-rocm:latest lanzado en la Bazzite (~10-15 GB)
- Pendiente: al terminar el pull → ejecutar el contenedor con el script →
  entrenamiento (~30-60 min estimados) → export GGUF q4_k_m → Mac


## 11. Evaluación del modelo entrenado hsmo-notas (16/09/2026)

ENTRENAMIENTO: completado en Bazzite (390 s, loss 1.735->1.327, 3 épocas).
GGUF q4_k_m 2.4 GB exportado y registrado en: (a) Ollama de la Mac
(disco lleno requirió liberar 3 GB: biblioteca 3D ya entregada en Bazzite),
(b) Ollama de la Bazzite (podman cp del GGUF).

RESULTADO DE LAS PRUEBAS (honesto):
- Petición simple: OK ("Sí" correcta)
- SOLO-user corto: OK (recomendaciones razonables, 1 s, 44 tokens)
- SOLO-user egreso completo: estructura institucional correcta PERO
  repite frases en cascada (sobreajuste con 139 ejemplos x 3 épocas)
  y inventa campos faltantes (fecha de egreso, apellido)
- System largo: EOS inmediato (artefacto: el modelo aprendió el patrón
  system->EOS del dataset con plantilla completa sin máscara)
- repeat_penalty 1.3: rompe la tokenización de palabras (no usar)
- COMPARATIVA: qwen3:14b con system anti-invención = redacción PERFECTA,
  fiel, sin repeticiones (24 s en GPU)

DECISIÓN: qwen3:14b sigue siendo el editor de egresos (con el system
prompt anti-invención del flujo). El modelo hsmo-notas (4B) queda
REGISTRADO en ambas máquinas como EXPERIMENTO y base para re-entrenar
cuando el dataset crezca (mejoras aplicables: train_on_responses_only
(enmascarar user), 2 épocas, más datos, num_predict limitado).

Mac Intel 8 GB: NO sirve para el 4B (4 peticiones 500 por RAM agotada
con Chrome+Hermes activos). El Mac Mini M5 Pro 24 GB evaluado por el
doctor resuelve esto (memoria unificada, qwen3:14b en GPU ~40-60 tok/s).
