# Inventario descargado — archivos fine tuning (16/09/2026)

Descarga rclone verificada: 343/343 objetos de Drive, 94 MB.

## Contenido confirmado
- 19 EGRESOS reales .docx (raíz) — EGRESO_APELLIDOS_NOMBRE.docx
- 1 PLANTILLA_DE_EGRESO_2026.docx (tabla 4x7 institucional)
- 318 notas de "DR DEMIANK /": 153 INDICACIONES, 87 evolución UCEP,
  14 consulta externa, 5 valoración, 1 urgencias, 58 otra
  (muchas son PARES nota→INDICAS: 21 pares completos detectados)
- 15 notas adicionales en "NOTAS DEMIANK/"

## Formato de los egresos (extraído del XML/textboxes)
Encabezado (nombre, FN, edad, género, CURP, expediente, fechas,
diagnósticos CIE-10 de ingreso/egreso, internamientos, estancia,
derechohabiencia) + RESUMEN MEDICO + EM + EF + SV + GABINETE +
MOTIVO DE EGRESO + PLAN DE MANEJO Y TRATAMIENTO (con medicamentos
y esquemas) + RECOMENDACIONES Y ATENCIÓN DE FACTORES DE RIESGO +
PRONÓSTICO + PROGRAMAR CITAS (7 servicios con SI/NO) + firma
Dr. Demian Nacim Kuri González 13406480.

## Decisión del doctor (16/09)
SIN anonimización (todo permanece en infraestructura local del doctor:
Mac + Bazzite; nunca sale a la nube).

## Siguiente fase
1. Extraer texto completo de las 342 notas + 19 egresos
2. Construir JSONL por tarea:
   - egresos (19; plantilla + estilo del doctor)
   - evoluciones SOAP (87 + 14 CE + 5 valoración)
   - indicaciones (21 pares nota→INDICAS; 117 INDICAS sueltas como
     contexto)
3. Fine-tuning qwen3:4b-instruct-2507 QLoRA 8-bit en Bazzite
