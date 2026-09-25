# Registro de exclusión — datos sensibles de pacientes y documentos de identidad

Estas rutas, dentro de `00_raw/Medicina/`, contienen o contenían expedientes clínicos con nombres reales de pacientes, historias clínicas, notas médicas, recetas o documentos de identidad personal. **Quedan permanentemente excluidas de lectura, síntesis y citación por la IA**, en cualquier fase de procesamiento de este vault.

Fecha de detección: 2026-07-08. Fecha de re-verificación: 2026-07-08 (segunda pasada, tras limpieza parcial de Demian).

## ✅ Ya movidas/eliminadas (verificado, ya no están en la carpeta)

- `DIAGNÓSTICOS HSMO.rar`
- `diagnosticos_repetidos.zip`
- `diagnosticos_agrupados.zip`, `diagnosticos_agrupados (1).zip`
- `DAYRA GENESIS CASTRO GUAL HC.xls`
- `MARGARITA AGUILAR GONZALEZ HC.xlsx`, `MARGARITA AGUILAR GONZALEZ HC CON HOJA DE NOTA.xlsx`
- `RAUL RODRIGUEZ SANTOS 31.12.2024.docx`, `RAUL RODRIGUEZ SANTOS 31.12.2024.pdf`
- `RAUL_RODRIGUEZ_SANTOS_EstructuraVisual.xlsx`, `RAUL_RODRIGUEZ_SANTOS_VisualMatch.xlsx`
- `Lista_de_pacientes.docx`, `Lista_de_pacientes_agosto_2025.docx`
- `Registro pacientes  actualizado.xlsx`, `Registro pacientes  actualizado agosto.xlsx`
- `PACIENTES CRONICOS  2024.docx`
- `Receta_Medica_Demian_Kuri.docx`, `Receta_Medica_Demian_Kuri_Media_Hoja.docx`, `Receta_Medica_Demian_Kuri_Media_Hoja.pdf`
- `RECETA.docx`, `RECETA PAQUE.docx`, `recetaa.docx`, `RECETA DEMINAK.pdf`
- `FORMATOS MOCEBPASS/HC_Psiquiatrica_MOCEBPASS_A6_HSMO*.xlsx` (v1 a v4)

## ⚠️ Todavía presentes en `00_raw/Medicina/` — pendientes de mover

**Expedientes y notas clínicas de pacientes (nombres reales):**
- `DIAGNÓSTICOS HSMO/` (carpeta completa, con subcarpetas F06, F15, F17, F19, F20, F25, F31, F33, F41, F43, F60, F71, F73)
- `DR DEMIANK/` (incluye `DR DEMIANK PARTE 2/`) y `DR DEMIANK.7z`
- `diagnosticos_repetidos/` (carpeta, aunque el .zip ya se eliminó)
- `villas_cronico/` y `villas_cronico.zip`
- `RODRGIGUEZ ESPINOZA LAURA.xlsx`
- `Estructura_Notas_RAUL_RODRIGUEZ_SANTOS.xlsx`
- Familia de archivos de censo diario: `FORMATO HOJA DIARIA HOSPITALIZACIÓN 22.04.25.xlsx`, `hoja diaria mejorada.docx`, `hoja_diaria_convertida.docx`, `hoja_diaria_pacientes_tablas_separadas.docx`, `hoja_diaria_similar_pdf.docx`, `hoja_diaria_textboxes.docx`, `hoja_diaria_textboxes_sin_bordes.docx`

**Certificados (datos de pacientes):**
- `Certificado médico.pdf`, `Certificado médico_OCR.pdf`, `Certificado_pediatrico_ejemplo.docx`

**Documentos de identidad personal (no de pacientes, pero sensibles):**
- `archivos enarm/IdentidadA.jpg`, `archivos enarm/IdentidadA.zip`, `archivos enarm/IdentidadA/`, `archivos enarm/IdentidadR.jpg`
- `archivos enarm/Foto.jpg`
- `archivos enarm/TítuloA.jpg`, `archivos enarm/TítuloElectrónico_DEMIAN NACIM KURI GONZALEZ_page-0001.jpg`, `archivos enarm/TítuloR.jpg`

## Acción recomendada

Mover lo que queda en la lista "⚠️ Todavía presentes" fuera de la carpeta `ENARM CEREBRO DEMIANK`, a una carpeta separada de expedientes clínicos con el resguardo de confidencialidad correspondiente. Ya avanzó bastante: de 33 rutas detectadas originalmente, quedan 17 (contando la carpeta `DIAGNÓSTICOS HSMO/` y `DR DEMIANK/` como una sola ruta cada una).

## Nota sobre alcance del procesamiento académico

Además de lo anterior, quedaron fuera del procesamiento académico de esta fase (por no ser material de estudio, no por ser dato sensible de paciente) los archivos administrativos del hospital: existencias de medicamentos, reglamentos internos, manuales MOCEBPASS, procedimientos institucionales, y los proyectos de doctorado de Salud_Mental_TAP pertenecientes a un tercero. Pueden incorporarse en una fase posterior si Demian lo solicita.
