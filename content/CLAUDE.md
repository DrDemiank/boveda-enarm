# CLAUDE.md — Constitución del sistema "ENARM Cerebro Demiank"

Este archivo define las reglas de comportamiento para cualquier modelo de lenguaje (Claude en Cowork, Claude Code, u otro) que opere sobre esta bóveda de Obsidian. Debe leerse por completo antes de procesar, crear o modificar cualquier archivo dentro de este vault.

## 1. Propósito del sistema

Esta bóveda es la base de conocimiento personal (second brain) de Demian Nacim Kuri González, médico general mexicano, para:

1. Preparar y aprobar el ENARM (Examen Nacional de Aspirantes a Residencias Médicas).
2. Consolidar conocimiento clínico de utilidad inmediata en su práctica en un hospital de salud mental.
3. Construir una base sólida orientada a su meta de especializarse en Psiquiatría.

El sistema sigue el patrón "LLM Wiki" (Karpathy, abril 2026): el conocimiento se compila una sola vez, se estructura y se mantiene actualizado de forma permanente, en lugar de recuperarse fragmentado desde cero en cada consulta.

## 2. Arquitectura de tres capas

| Capa | Carpeta | Quién escribe | Regla |
|---|---|---|---|
| 1. Fuentes inmutables | `00_raw/` | Solo el humano (Demian) | La IA tiene **prohibido terminantemente** modificar, editar, mover, renombrar o borrar cualquier archivo dentro de `00_raw/`. Es la fuente absoluta de la verdad. |
| Bandeja de entrada | `01_inbox/` | El humano deposita notas rápidas o fuentes sin clasificar | La IA puede leer, clasificar y mover el *contenido procesado* hacia `00_raw/` (fuente) y `02_wiki/` (síntesis), pero nunca debe alterar el archivo original antes de archivarlo. |
| 2. Wiki dinámica | `02_wiki/` | La IA (lectura para el humano) | La IA lee `00_raw/`, extrae entidades, genera resúmenes, crea enlaces bidireccionales `[[concepto]]` y mantiene los índices (MOC). El humano lee y puede anotar, pero la estructura y el enlazado son responsabilidad de la IA. |
| 3. Configuración | `CLAUDE.md` (este archivo) | Solo el humano | Define taxonomía, nomenclatura y reglas. La IA no debe modificar este archivo salvo instrucción explícita de Demian. |
| Bitácora | `_logs/` | La IA | Registro de fuentes procesadas, contradicciones detectadas y cambios relevantes. |

## 3. Regla de operación principal

- **El humano** cura las fuentes (deposita PDFs, artículos, transcripciones, GPC, capturas de pantalla, apuntes) en `00_raw/` o `01_inbox/`, dirige el análisis y formula preguntas de alto valor.
- **La IA** hace todo lo demás: organiza, enlaza, mantiene el índice, audita el estado de los archivos y sintetiza respuestas citando siempre la fuente original.

## 4. Taxonomía de notas en `02_wiki/`

Toda nota nueva debe clasificarse en una de estas categorías (subcarpeta correspondiente):

- `conceptos/` — Conceptos transversales (p. ej. `Inhibidores Selectivos de la Recaptura de Serotonina.md`, `Eje Hipotálamo-Hipófisis-Suprarrenal.md`).
- `patologias/` — Entidades nosológicas (p. ej. `Trastorno Depresivo Mayor.md`, `Esquizofrenia.md`).
- `farmacologia/` — Fármacos individuales, con dosis, indicaciones, contraindicaciones, efectos adversos (p. ej. `Sertralina.md`).
- `casos_clinicos/` — Síntesis de casos clínicos revisados o discutidos.
- `indices/` — Mapas de contenido (MOC) por especialidad ENARM: Psiquiatría, Medicina Interna, Cirugía, Pediatría, Ginecología y Obstetricia, Salud Pública, Urgencias. Cada MOC enlaza a todas las notas relacionadas de esa especialidad.

### Nomenclatura de archivos

- Nombre del archivo = título exacto del concepto/entidad, en español, con mayúscula inicial por palabra relevante (Title Case), sin abreviaturas ambiguas. Ejemplo: `Trastorno Bipolar Tipo I.md`, no `TB1.md`.
- Evitar duplicados: antes de crear una nota nueva, verificar si ya existe un archivo equivalente (considerar sinónimos y abreviaturas médicas comunes en español).

### Frontmatter obligatorio (YAML) en cada nota de `02_wiki/`

```yaml
---
tipo: concepto | patologia | farmacologia | caso_clinico | indice
especialidad: [Psiquiatria, Medicina_Interna, Cirugia, Pediatria, GinecoObstetricia, Salud_Publica, Urgencias]
tags: [ENARM]
fuentes: ["[[nombre-del-archivo-en-00_raw]]"]
fecha_creacion: YYYY-MM-DD
fecha_actualizacion: YYYY-MM-DD
estado: borrador | revisado
---
```

## 5. Reglas de enlazado

- Toda mención de un concepto que tenga (o deba tener) su propia nota se enlaza con `[[Nombre Exacto de la Nota]]`.
- Cada nota nueva debe enlazarse desde el MOC de especialidad correspondiente en `02_wiki/indices/`.
- Preferir enlaces bidireccionales naturales (Obsidian genera backlinks automáticamente); no es necesario duplicar manualmente la lista de "notas relacionadas", salvo para relaciones no obvias (p. ej. comorbilidades, diagnósticos diferenciales).

## 6. Manejo de contradicciones

Si al procesar una fuente nueva se detecta una contradicción con contenido ya existente en `02_wiki/` (p. ej. un rango de dosis distinto, un criterio diagnóstico actualizado):

1. **No sobrescribir silenciosamente.** Conservar ambas versiones dentro de la nota, señalando claramente el conflicto.
2. Añadir una sección `## ⚠️ Contradicción detectada` en la nota afectada, citando ambas fuentes (Vancouver) y la fecha de cada una.
3. Registrar el hallazgo en `_logs/contradicciones.md` con fecha, nota afectada y breve descripción.
4. Nunca decidir de forma autónoma cuál fuente es "correcta"; el humano resuelve la contradicción.

## 7. Estilo, idioma y citación (reglas inquebrantables)

- Todo el contenido generado se redacta en español, con tono formal, detallado, amplio y neutral. Sin opiniones personales no solicitadas. Sin tono dramático ni excesivamente entusiasta.
- Toda nota que contenga información médica o académica debe estar fundamentada con referencias bibliográficas en **formato Vancouver**, en español.
- **Regla inquebrantable:** omitir y eliminar siempre la palabra "[Internet]" de cualquier cita.
- Máximo 15 fuentes relevantes por nota cuando se condensa información extensa.
- Al redactar respuestas dirigidas a terceros (réplicas de foro, mensajes a colegas), usar siempre el pronombre "usted", en tono constructivo y no confrontativo.

## 8. Flujo de trabajo (procesamiento de fuentes)

Cuando Demian indique "procesa las fuentes nuevas" o equivalente, la IA debe:

1. Revisar `01_inbox/` y `00_raw/` en busca de archivos no registrados en `_logs/bitacora.md`.
2. Leer cada fuente nueva por completo.
3. Extraer entidades, conceptos clave, criterios diagnósticos, algoritmos de tratamiento y rangos de dosificación cuando aplique.
4. Crear o actualizar las notas correspondientes en `02_wiki/` siguiendo la taxonomía y el frontmatter de este documento.
5. Enlazar bidireccionalmente y actualizar el MOC de especialidad correspondiente.
6. Señalar contradicciones según la sección 6.
7. Registrar en `_logs/bitacora.md`: fecha, archivo procesado, notas creadas/actualizadas.
8. Al finalizar, entregar a Demian un resumen breve de lo procesado (qué se creó, qué se actualizó, qué contradicciones se detectaron).

## 9. Auditoría periódica ("lint" de la wiki)

Cuando Demian lo solicite, la IA debe revisar `02_wiki/` en busca de:

- Enlaces rotos (`[[notas]]` que no existen).
- Notas huérfanas (sin ningún enlace entrante).
- Vacíos de contenido evidentes en el temario ENARM (especialidades o subtemas sin notas).
- Notas en estado `borrador` que llevan mucho tiempo sin revisión.

Reportar hallazgos en texto plano al humano; no corregir automáticamente sin confirmación cuando la corrección implique eliminar contenido.

## 10. Prohibiciones explícitas

- No modificar, mover ni borrar ningún archivo de `00_raw/`.
- No inventar dosis, criterios diagnósticos o datos clínicos que no consten en las fuentes curadas. Si la fuente no es clara, señalarlo explícitamente en la nota en lugar de completar con conocimiento general del modelo.
- No usar fuentes de internet no curadas por Demian para responder preguntas de estudio; la síntesis debe basarse estrictamente en lo depositado en `00_raw/`, salvo que Demian pida explícitamente una búsqueda externa.
