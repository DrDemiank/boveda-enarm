---
tipo: configuracion
version: 1.0
fecha_creacion: 2026-07-10
fecha_actualizacion: 2026-07-10
---

# PROMPT MAESTRO — Sistema Multi-IA para "ENARM Cerebro Demiank"

## 0. Propósito de este documento

`CLAUDE.md` (en la raíz de esta bóveda) es la constitución del sistema: define taxonomía, nomenclatura, citación y reglas inquebrantables. Ese archivo NO se modifica con este documento ni se duplica su contenido aquí.

Este documento (`PROMPT MAESTRO`) es la capa complementaria que permite operar el mismo sistema con **más de una inteligencia artificial** — no solo con Claude/Cowork — para que Demian pueda:

1. Continuar el trabajo con otra IA (ChatGPT, Gemini, DeepSeek, un modelo local vía Ollama, etc.) cuando se agoten los créditos o tokens de la IA principal.
2. Comparar objetivamente cómo distintas IAs ejecutan la misma clase de tareas sobre esta bóveda.
3. Dejar un registro (bitácora + evaluación) de qué IA hizo qué, y con qué calidad, para poder auditar el contenido con el tiempo.

Toda IA que trabaje en esta bóveda —sin excepción— debe leer primero `CLAUDE.md` completo y luego este documento.

## 1. Contexto del sistema (resumen)

- Dueño de la bóveda: Demian Nacim Kuri González, médico general mexicano, labora en un hospital de salud mental, meta profesional: especializarse en Psiquiatría.
- Objetivo de la bóveda: preparación para el ENARM siguiendo el patrón "LLM Wiki" (conocimiento compilado una sola vez, estructurado y mantenido, no recuperado fragmentado en cada consulta).
- Arquitectura de tres capas: `00_raw/` (fuentes inmutables, solo las toca el humano), `01_inbox/` (bandeja de entrada), `02_wiki/` (síntesis generada y mantenida por la IA), `_logs/` (bitácora, contradicciones, exclusión de datos sensibles, y ahora evaluación multi-IA).
- El detalle completo de taxonomía, frontmatter YAML, nomenclatura de archivos y reglas de citación está en `CLAUDE.md` — no se repite aquí para evitar que ambos documentos se desincronicen. Ante cualquier duda, `CLAUDE.md` es la fuente de verdad.

## 2. Reglas inquebrantables (recordatorio operativo)

Estas reglas aplican **igual para cualquier IA**, sin excepción, y están desarrolladas en detalle en `CLAUDE.md`:

- Prohibido modificar, mover o borrar cualquier archivo de `00_raw/`.
- Toda nota nueva en `02_wiki/` lleva el frontmatter YAML obligatorio (`tipo`, `especialidad`, `tags`, `fuentes`, `fecha_creacion`, `fecha_actualizacion`, `estado`).
- Prohibido inventar datos clínicos (dosis, criterios diagnósticos, cifras) que no consten en la fuente curada. Si la fuente es ambigua o ilegible, se señala explícitamente como "Nota de verificación" en vez de completarse con conocimiento general del modelo.
- Las contradicciones entre fuentes nunca se resuelven en automático ni se sobrescriben: se documentan ambas versiones bajo `## ⚠️ Contradicción detectada`, se citan ambas fuentes, y se registra el hallazgo en `_logs/contradicciones.md`. Solo Demian decide cuál es correcta.
- Toda nota médica/académica lleva referencias en formato Vancouver, en español, sin la palabra "[Internet]", máximo 15 fuentes relevantes por nota.
- Al redactar textos dirigidos a terceros (foros, mensajes a colegas), usar siempre "usted", tono constructivo.

## 3. Prompt de arranque ("bootstrap") — copiar y pegar en cualquier IA nueva

Cuando Demian abra una sesión con otra IA (ChatGPT, Gemini, DeepSeek, un modelo local en Ollama/LM Studio, etc.) para continuar el trabajo en esta bóveda, debe copiar y pegar el siguiente bloque como primer mensaje, ajustando la sección entre corchetes según corresponda:

```
Vas a operar como asistente de conocimiento sobre una bóveda de Obsidian
llamada "ENARM Cerebro Demiank", propiedad de un médico general mexicano
que se prepara para el examen ENARM con meta de especializarse en
Psiquiatría.

La bóveda sigue el patrón "LLM Wiki": fuentes inmutables en 00_raw/,
síntesis mantenida por IA en 02_wiki/, reglas fijas en CLAUDE.md
(ubicado en la raíz de la bóveda).

ANTES de hacer cualquier cosa, debes leer completo el archivo CLAUDE.md
de la raíz y seguirlo al pie de la letra. Sus reglas más importantes:
- Nunca modifiques, muevas ni borres nada dentro de 00_raw/.
- Toda nota nueva en 02_wiki/ lleva un frontmatter YAML con: tipo,
  especialidad, tags, fuentes, fecha_creacion, fecha_actualizacion,
  estado.
- Nunca inventes datos clínicos (dosis, criterios diagnósticos, cifras)
  que no estén en la fuente que te doy. Si algo es ilegible o ambiguo,
  dilo explícitamente como "Nota de verificación" en vez de rellenarlo
  con tu conocimiento general.
- Si detectas una contradicción entre lo que ya existe en la wiki y la
  fuente nueva, NO la resuelvas ni sobrescribas: documenta ambas
  versiones bajo un encabezado "## ⚠️ Contradicción detectada", cita
  ambas fuentes, y dímelo explícitamente en tu respuesta para que yo lo
  registre.
- Toda nota médica lleva referencias en formato Vancouver en español,
  sin la palabra "[Internet]", máximo 15 fuentes por nota.

[Si esta IA SÍ tiene acceso a archivos/carpeta local:]
Tienes acceso a la carpeta de la bóveda en [ruta]. Trabaja
directamente sobre los archivos.

[Si esta IA NO tiene acceso a archivos (chat puro, sin herramientas):]
No tienes acceso a mis archivos. Yo te voy a pegar el contenido de las
fuentes y de las notas existentes que necesites revisar. Cuando termines
una nota, dámela completa en un bloque de código markdown, con el
frontmatter incluido, lista para que yo la guarde con el nombre exacto
que me indiques (Title Case en español, sin abreviaturas ambiguas).

Al terminar tu tarea, dame un resumen en texto plano de: qué notas
creaste o modificaste, qué contradicciones detectaste (si las hubo), y
qué datos dejaste marcados como "Nota de verificación" por ser
ilegibles o ambiguos en la fuente. No necesito explicaciones largas de
tu proceso, solo esa lista.

Mi tarea de hoy es: [describir la tarea específica, por ejemplo:
"robustecer las notas de Cirugía a partir de las páginas X-Y del manual
Prieto, que te voy a pegar a continuación"].
```

## 4. Adaptaciones según el tipo de IA

No todas las IAs tienen las mismas capacidades. Antes de empezar, identifica en cuál de estos dos grupos está la IA que vas a usar:

**A. IA con acceso a archivos/carpeta** (Claude en Cowork o Claude Code, agentes con herramientas de sistema de archivos, algunos asistentes locales con plugins de archivos): puede leer y escribir directamente en la bóveda. Es el escenario preferido — es el que se ha usado hasta ahora.

**B. IA de solo chat, sin acceso a archivos** (ChatGPT web, Gemini web, DeepSeek web, la mayoría de interfaces de chat sin plugins): Demian debe copiar y pegar manualmente el contenido de las fuentes (`00_raw/`) y de las notas relevantes (`02_wiki/`), y luego copiar el resultado que la IA entregue de vuelta a un archivo `.md` nuevo o existente. Es más lento, pero funciona igual de bien para tareas acotadas (una nota, un par de notas relacionadas).

**C. IA local (Ollama, DeepSeek local, modelos autoalojados)**: revisar primero si el modelo tiene ventana de contexto suficiente para el fragmento de fuente que se le va a dar (los extractos OCR de los manuales pueden ser largos). Si el modelo es pequeño, es preferible darle fragmentos cortos y una sola nota a la vez, en vez de lotes grandes como los que se usan con Claude.

Para tareas grandes (procesar una especialidad completa, un lote de OCR extenso), el patrón que ha funcionado bien es dividir el trabajo en fragmentos por tema/rango de páginas y asignar cada fragmento a una sesión o "subagente" distinto — esto aplica tanto si se usan subagentes de Claude como si se abren varias pestañas/conversaciones en paralelo con otra IA.

## 5. Protocolo de relevo entre IAs (handoff)

Cuando se cambia de una IA a otra a mitad de una tarea (por ejemplo, se acabaron los tokens de Claude y se continúa con otra IA), seguir este orden:

1. **Verificar en disco, no confiar en el resumen de la IA anterior.** Antes de asumir qué se hizo, listar los archivos realmente existentes en `02_wiki/` y comparar contra la lista de temas que se pretendía cubrir. Las IAs pueden reportar más o menos de lo que efectivamente guardaron, especialmente si la sesión se cortó a mitad de tarea.
2. **Dar a la nueva IA solo lo que falta.** No le repitas trabajo ya hecho: dile explícitamente qué notas ya existen (para que las revise y complemente si aplica, en vez de duplicarlas) y cuáles faltan por crear.
3. **Mantener la misma fuente de verdad.** La nueva IA debe trabajar sobre el mismo extracto de fuente (mismo archivo OCR, mismo PDF, mismo rango de páginas) que se venía usando, para que el contenido sea consistente.
4. **Registrar el relevo en la bitácora.** Al terminar, anota en `_logs/bitacora.md` qué IA hizo cada bloque de trabajo (ver plantilla ampliada en la sección 7).

## 6. Errores conocidos y lecciones aprendidas (para que no se repitan)

- El OCR de manuales escaneados (páginas sin capa de texto) es lento y propenso a errores en tablas y cifras numéricas. Cualquier IA que reciba texto OCR debe tratar las tablas con especial cautela y marcar como "Nota de verificación" cualquier celda dudosa, en vez de reconstruirla por inferencia.
- Las sesiones con límite de tiempo o de tokens pueden cortarse a mitad de una tarea larga. Por eso la instrucción de "guardar cada nota completa antes de pasar a la siguiente" es importante con cualquier IA: minimiza el trabajo perdido si la sesión se interrumpe.
- El índice impreso de un manual no siempre coincide con el orden real del contenido, y los encabezados de sección no siempre se reconocen bien por OCR (pueden aparecer con caracteres sueltos como "I" o "|" pegados). Conviene revisar el texto fuente de forma corrida, no solo buscar encabezados en mayúsculas, para no perderse subtemas.
- Cuando una fuente remite a "otro volumen" o "otra sección" sin desarrollar el contenido, la nota correspondiente debe quedar en `estado: borrador` con una nota de verificación explicando por qué, en vez de inventar contenido para completarla.

## 7. Rúbrica de evaluación del desempeño de cada IA

Después de cada sesión de trabajo con una IA (Claude o cualquier otra), califica su desempeño con esta rúbrica de 1 a 5 (1 = no cumplió, 5 = cumplió completamente). Sirve para decidir con qué IA conviene dejar qué tipo de tarea.

| Criterio | Descripción | Puntaje (1-5) |
|---|---|---|
| Respeto a `00_raw/` | No modificó, movió ni borró nada de las fuentes inmutables | |
| Frontmatter y taxonomía | Usó el YAML completo y clasificó la nota en la carpeta correcta | |
| Nomenclatura de archivos | Nombre del archivo en Title Case español, sin abreviaturas ambiguas, sin duplicados | |
| Fidelidad a la fuente | No inventó dosis, cifras ni criterios diagnósticos; marcó lo ilegible como "Nota de verificación" | |
| Manejo de contradicciones | Si aplicaba, documentó ambas versiones sin sobrescribir y lo reportó explícitamente | |
| Citación Vancouver | Formato correcto, en español, sin la palabra "[Internet]" | |
| Enlazado y organización | Usó `[[enlaces]]` correctos a notas existentes y relacionadas, actualizó el MOC correspondiente | |
| Profundidad clínica | El contenido es suficientemente completo para estudio de ENARM, no superficial | |
| Seguimiento de instrucciones | Hizo exactamente lo pedido, sin desviarse ni omitir alcance sin avisar | |
| Honestidad del reporte final | Lo que reportó como hecho coincide con lo que realmente quedó guardado en disco | |

**Promedio de la sesión:** ____ / 5

**Observaciones libres:** (qué tan verboso fue, si hubo que corregirle algo manualmente, si convendría usarla de nuevo para este tipo de tarea, etc.)

## 8. Bitácora multi-IA — plantilla ampliada

A partir de ahora, cuando una IA distinta de Claude procese fuentes o cree/modifique notas, se registra en `_logs/bitacora.md` con una columna adicional de IA utilizada, usando esta plantilla de fila:

```
| Fecha | IA utilizada | Fuente procesada | Notas creadas | Notas actualizadas |
|---|---|---|---|---|
| YYYY-MM-DD | Claude / ChatGPT / Gemini / DeepSeek / Ollama (modelo) / otra | ... | ... | ... |
```

Si la bitácora existente no tiene aún esta columna, se agrega solo en las filas nuevas (no hace falta reescribir el historial previo, todo lo procesado hasta el 2026-07-09 fue con Claude).

Además, se sugiere llevar el detalle de cada evaluación (sección 7) en un archivo separado `_logs/evaluacion_ias.md`, con una entrada por sesión, para poder comparar el desempeño acumulado de cada IA a lo largo del tiempo.

## 9. Cuándo usar cuál IA (guía práctica)

- **Tareas grandes, con muchos archivos fuente y necesidad de organizar/enlazar la wiki completa:** preferir una IA con acceso directo a archivos y capacidad de trabajar en lotes/subagentes (como Claude en Cowork), por la cantidad de contexto y pasos involucrados.
- **Tareas puntuales y acotadas (una nota, ampliar una nota existente con una fuente corta):** cualquier IA de chat funciona bien, incluso sin acceso a archivos, copiando y pegando.
- **Cuando se agoten los tokens de la IA principal a mitad de un lote grande:** seguir el protocolo de relevo (sección 5) con la siguiente IA disponible, dándole solo el trabajo pendiente.
- **Para segundas opiniones o detección de contradicciones:** puede ser útil pedirle a una segunda IA que revise una nota ya creada por otra, sin decirle qué IA la hizo, y comparar si detecta los mismos datos o inconsistencias — esto ayuda a evaluar de forma más objetiva.
