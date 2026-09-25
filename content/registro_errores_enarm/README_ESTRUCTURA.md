# Estructura del registro de errores ENARM

Cada especialidad ENARM procesada tendrá su carpeta con 3 subcarpetas internas:

    registro_errores_enarm/
    └── <Especialidad>/
        ├── 01_preguntas/    ← preguntas transcritas + caso clínico + respuesta correcta
        │                      (grupos con caso compartido van juntos; archivos de ~100 preguntas)
        ├── 02_resumenes/    ← resúmenes didácticos del profesor, por temas de 10
        └── 03_analisis/     ← por qué me equivoqué y qué hacer para mejorar (+ técnica T1-T13)

Especialidades posibles: Psiquiatria · Cirugia · Pediatria · GinecoObstetricia ·
Medicina_Interna · Salud_Publica · Urgencias

Las carpetas se crean bajo demanda, solo de la especialidad del examen procesado.
Este README no es conocimiento: es la convención de organización (actualizada 07/09/2026).
