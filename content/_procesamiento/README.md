---
tipo: configuracion
fecha_creacion: 2026-07-10
fecha_actualizacion: 2026-07-10
---

# `_procesamiento/` — Capa intermedia de análisis (PDF → Wiki)

Esta carpeta es la capa técnica que faltaba entre `01_inbox/` (donde Demian deposita los PDF) y `02_wiki/` (donde queda la síntesis final). Antes, el texto extraído de los manuales (sobre todo el que requería OCR) se generaba en el espacio de trabajo temporal de la IA y se perdía al cerrar la sesión. Ahora queda guardado aquí, dentro de la bóveda, visible en Obsidian y disponible para cualquier IA que retome el trabajo después.

## Flujo completo, en tres capas

```
01_inbox/                    02_procesamiento/               02_wiki/
(Demian deposita el PDF) →   (la IA extrae y guarda el   →   (la IA redacta/actualiza
                              texto crudo por lote/tema)      las notas finales)
```

1. **`01_inbox/`** — Demian coloca aquí el PDF nuevo (un libro, una GPC, un artículo). Si el PDF ya es una fuente académica curada y confiable, se archiva en `00_raw/` (intacta, sin modificar — ver `CLAUDE.md` sección 2); `01_inbox/` es solo la bandeja de entrada antes de esa clasificación.

2. **`_procesamiento/`** — Aquí la IA guarda el texto ya extraído del PDF, antes de convertirlo en notas de wiki. Cada lote de trabajo tiene su propia subcarpeta, nombrada `AAAA-MM-DD_tema_fuente/`, con uno o varios archivos `.txt` que contienen el texto plano extraído, casi siempre con marcadores `===PAGE N===` para conservar la referencia a la página original del PDF. Esta carpeta es la "bitácora de trabajo" del análisis: permite auditar exactamente qué texto se usó para redactar cada nota, y permite retomar el trabajo sin repetir la extracción (que puede tardar varios minutos si el PDF requiere OCR).

3. **`02_wiki/`** — Destino final. La IA lee el `.txt` de `_procesamiento/`, lo contrasta con lo que ya existe en `02_wiki/` (para no duplicar), y redacta o amplía las notas correspondientes siguiendo la taxonomía, el frontmatter y las reglas de citación de `CLAUDE.md`. Al terminar, actualiza el MOC de la especialidad y registra el trabajo en `_logs/bitacora.md`.

## Cómo se decide si un PDF necesita OCR

Antes de extraer texto de un PDF nuevo, la IA prueba a leer un par de páginas de muestra:

- Si el PDF tiene capa de texto (la mayoría de los PDF "nativos", no escaneados): la extracción es directa e inmediata.
- Si el PDF es un escaneo de páginas (imágenes, sin capa de texto — común en libros fotocopiados o escaneados): hace falta un paso de OCR (reconocimiento óptico de caracteres) página por página antes de poder trabajar el contenido. Esto es más lento (varios segundos por página) y con más posibilidad de errores de reconocimiento, sobre todo en tablas y cifras numéricas — por eso cualquier dato dudoso se marca como "Nota de verificación" en la nota final en vez de adivinarse.

## Cómo se localiza el tema dentro de un libro grande

Los manuales de estudio (como el Manual Dr. Prieto) traen un índice al inicio con la lista de temas y su número de página "impreso". Ese número casi nunca coincide exactamente con la posición real del archivo PDF (por las páginas de portada, agradecimientos, etc. que se cuentan aparte). La IA calcula ese desfase comparando el índice contra el contenido real de un par de páginas de muestra, y así ubica el rango exacto de páginas físicas del PDF que corresponde al tema pedido, antes de extraer solo ese rango (no el libro completo).

## Lotes ya procesados en esta carpeta

- `2026-07-08_medicina_interna_prieto/` — extractos de cardiopatía isquémica, anemias, hepatopatías, tiroides, asma/EPOC y EVC del Manual Dr. Prieto (con capa de texto, sin OCR).
- `2026-07-08_ginecologia_obstetricia_prieto/` — extracto completo de la sección Ginecología y Obstetricia del Manual Dr. Prieto (páginas escaneadas, requirió OCR completo).
- `2026-07-09_pediatria_prieto/` — extracto completo de la sección Pediatría del Manual Dr. Prieto (páginas escaneadas, requirió OCR completo).

## Cómo pedir un nuevo lote

Basta con decir, por ejemplo: "procesa el PDF de [nombre] que dejé en 01_inbox/, para robustecer [especialidad/tema]". La IA se encarga de: ubicarlo, decidir si necesita OCR, localizar el rango de páginas relevante, extraer el texto a esta carpeta, redactar/ampliar las notas en `02_wiki/`, actualizar el MOC correspondiente y dejar el registro en `_logs/bitacora.md`.

## Nota sobre `CLAUDE.md`

Esta carpeta es una adición operativa al sistema descrito en `CLAUDE.md`, pero no lo reemplaza: todas las reglas de esa constitución (no tocar `00_raw/`, frontmatter obligatorio, no inventar datos, manejo de contradicciones, citación Vancouver) siguen aplicando exactamente igual sobre el contenido que termina en `02_wiki/`. Si quieres que esta carpeta quede formalizada dentro de la tabla de arquitectura de `CLAUDE.md` (sección 2), dímelo explícitamente y la agrego ahí — por ahora no se modificó ese archivo porque la constitución indica que solo tú debes editarlo.
