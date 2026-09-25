# Dataset de egresos HSMO — entrenamiento Fase 2

Reglas del plan (plan-modelo-local-bazzite.md):
- Anonimización ANTES de que el dato toque el disco: nombres, expedientes,
  CURP, fechas de nacimiento exactas, domicilios, teléfonos, familiares.
  Se sustituyen por datos ficticios CONSISTENTES (sin huecos).
- Formato JSONL conversacional: {"messages": [system, user(JSON 29 campos), assistant(egreso final aprobado)]}
- 10-15% se separa como conjunto de prueba (el modelo nunca lo ve).
- Este directorio NO sale de la Mac salvo anonimizado; el entrenamiento
  corre en la Bazzite.

Estructura:
- ejemplos_reales/ — las hojas que el doctor envía (originales, con
  identificador interno para su propia referencia)
- dataset_train.jsonl — pares (JSON → egreso aprobado) anonimizados
- dataset_test.jsonl — separación para evaluación

Flujo por cada hoja nueva:
1. El doctor envía la hoja (foto o PDF) por Telegram
2. La Mole la lee y arma el JSON de 29 campos (reglas anti-invensión)
3. La Mole anonimiza y escribe el par JSONL
4. El doctor valida la redacción → solo entonces queda como ejemplo


## Estructura ampliada (16/09) — carpeta Drive "archivos fine tuning"

La carpeta Drive del doctor contiene: egresos reales, ~400 notas de
evolución variadas (con SOAP completo), la plantilla de egresos
institucional y las instrucciones de cómo el doctor hace los egresos.

Tareas de entrenamiento definidas:
1. EGRESOS: nota/expediente → hoja de egreso (plantilla + instrucciones
   del doctor como guía de estilo)
2. EVOLUCIONES SOAP: datos de la entrevista → nota SOAP en su estilo
   (S: subjetivo, O: objetivo, A: diagnóstico/analisis, P: plan)
3. INDICACIONES: si hay estructura en la carpeta → indicaciones
   médicas en su formato
4. PLANTILLA: la plantilla institucional va en plantillas/ y se usa
   como referencia fija en el system prompt del fine-tuning

Regla de conteo: validar el número de archivos descargados contra lo
que el doctor declara antes de procesar (anti-pérdida).

Anti-invención ampliada: las instrucciones del doctor sobre cómo hace
los egresos son REGLA (la plantilla y su proceso prevalecen); el modelo
aprende a imitarlas, nunca a contradecirlas.
