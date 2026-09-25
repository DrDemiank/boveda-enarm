---
tipo: registro
tags: [ENARM, banco_preguntas, procesamiento]
fecha_actualizacion: 2026-07-21
---

# Estado de Procesamiento — Banco de Preguntas ENARM 2026

## Resumen

- **PDF fuente:** `~/Downloads/preguntas enrm 2026.pdf` (100 páginas)
- **Total de preguntas extraídas:** 529
- **Preguntas clasificadas:** 427
- **Preguntas pendientes:** 102
- **Páginas procesadas:** 100/100 (completado)
- **Imágenes procesadas:** `/tmp/enarm_pdf_tiny/pagina_001.jpg` a `pagina_100.jpg`

## Clasificación por especialidad

| Especialidad | Preguntas |
|---|---|
| Gastroenterología | 64 |
| Pediatría | 56 |
| Cardiología | 39 |
| Hematología | 32 |
| Neumología | 28 |
| Infectología | 25 |
| Salud Pública | 24 |
| Gineco-Obstetricia | 20 |
| Endocrinología | 18 |
| Farmacología | 15 |
| Inmunología | 15 |
| Psiquiatría | 14 |
| Oftalmología | 12 |
| Cirugía | 11 |
| Neurología | 11 |
| Otorrinolaringología | 10 |
| Oncología | 9 |
| Nefrología | 7 |
| Reumatología | 7 |
| Anatomía | 5 |
| Dermatología | 5 |
| **Pendientes** | **102** |

## Archivos generados

- `banco_preguntas_consolidado.json` — JSON con 529 preguntas (229 KB)
- `banco_preguntas_clasificado.json` — JSON con clasificación por especialidad
- `preguntas_nuevas_51_78.json` — Lote 51-78 (156 preguntas)
- `preguntas_nuevas_79_100.json` — Lote 79-100 (133 preguntas)
- `02_wiki/banco_preguntas/Banco de Preguntas - *.md` — 22 archivos por especialidad

## Historial de procesamiento

- 2026-07-19: Páginas 1-50 procesadas (240 preguntas)
- 2026-07-21: Páginas 51-78 procesadas (156 preguntas, total 396)
- 2026-07-21: Páginas 79-100 procesadas (133 preguntas, total 529)
- 2026-07-21: Clasificación actualizada y archivos de bóveda regenerados

## Notas

- Página 60 falló inicialmente por Connection error; se procesó en reintento
- Páginas 95, 97, 98, 99 fallaron por timeout en primer intento; se procesaron individualmente
- Algunas preguntas tienen numeración no secuencial en el original (ej. 416 aparece dos veces, 588 entre 597 y 599)
- Las 102 preguntas pendientes requieren revisión manual para clasificación fina