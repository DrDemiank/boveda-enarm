# Bitácora de procesamiento

Registro de fuentes procesadas de `00_raw/` y `01_inbox/` hacia `02_wiki/`.

| Fecha | Fuente procesada | Notas creadas | Notas actualizadas |
|---|---|---|---|
| 2026-07-08 | `00_raw/Medicina/Demiank Brain/MEDICINA INTERNA/PSIQUIATRÍA/` (128 notas atómicas) + `00_raw/Medicina/Sindrome_Neuroleptico_Maligno.md` + `00_raw/Medicina/Demiank Brain/DEFINICIÓN SINDROME NEUROLEPTICO MALIGNO.md` (vacía) | `Trastorno Depresivo Mayor.md`, `Esquizofrenia.md`, `Trastorno de Ansiedad Generalizada.md`, `Crisis de Angustia (Trastorno de Pánico).md`, `Trastorno Obsesivo Compulsivo.md`, `Síndrome Neuroléptico Maligno.md`, `Antipsicóticos Típicos.md`, `Antipsicóticos Atípicos.md`, `Terapia Electroconvulsiva.md`, `Terapia Cognitivo-Conductual.md`, `Trastornos de Ansiedad.md` | `MOC - Psiquiatria.md` |
| 2026-07-08 | `00_raw/Medicina/Demiank Brain/GINECOLOGÍA/` (17 notas atómicas) | `Menopausia.md`, `Gonorrea.md`, `Clamidiasis (Chlamydia trachomatis).md`, `Sífilis (Treponema pallidum).md`, `Tricomoniasis (Trichomonas vaginalis).md`, `Infección por Virus de la Inmunodeficiencia Humana (VIH).md`, `Infección por Virus del Papiloma Humano (VPH).md` | `MOC - Gineco-Obstetricia.md` |
| 2026-07-08 | `00_raw/Medicina/Demiank Brain/MEDICINA INTERNA/MEDICINA INTERNA/` (25 notas, incluye notas ya polidas de ERC, Nefropatía Diabética, SDRA, Sepsis y HAS) | `Amiloidosis.md`, `Diabetes Mellitus Tipo 2.md`, `Enfermedad Renal Crónica.md`, `Nefropatía Diabética.md`, `Síndrome de Dificultad Respiratoria Aguda.md`, `Sepsis y Choque Séptico.md`, `Hipertensión Arterial Sistémica.md` | `MOC - Medicina Interna.md` |
| 2026-07-08 | `00_raw/Medicina/Demiank Brain/PEDIATRÍA/` (103 notas atómicas, procesadas vía subagente) | `Cardiopatías Congénitas.md`, `Trastornos de la Diferenciación Sexual.md`, `Persistencia del Conducto Arterioso (PCA).md`, `Comunicación Interauricular (CIA).md`, `Comunicación Interventricular (CIV).md`, `Comunicaciones Auriculoventriculares.md`, `Tetralogía de Fallot.md`, `Anomalía de Ebstein.md`, `Transposición de Grandes Vasos (TGV).md`, `Coartación Aórtica.md`, `Síndrome de Eisenmenger.md`, `Anormalidades del Tracto Urinario y Genital.md`, `Enfermedad Diarreica Aguda.md`, `Enfermedades Exantemáticas.md`, `Estenosis Pilórica Hipertrófica.md`, `Faringoamigdalitis Bacteriana.md` | `MOC - Pediatria.md` |
| 2026-07-08 | `00_raw/Medicina/Demiank Brain/CIRUGÍA/` (112 notas atómicas + 4 imágenes de escalas, procesadas vía subagente) | `Traumatismo Craneoencefálico.md`, `Trauma Torácico.md`, `Trauma Abdominal.md`, `Trauma Pélvico.md`, `Trauma Raquimedular y Síndromes Medulares.md`, `Trauma Maxilofacial.md`, `Trauma Nasal.md`, `Trauma de Cuello.md`, `Quemaduras.md`, `Lesiones Graves por Electricidad.md`, `Mordeduras y Picaduras.md`, `Atención Inicial del Paciente Politraumatizado.md`, `Escala de Coma de Glasgow.md`, `Muerte Cerebral.md`, `Regla de los 9 de Wallace y Esquema de Lund and Browder.md`, `Grado de Displasia Renal.md` (borrador) | `MOC - Cirugia.md` |
| 2026-07-08 | `00_raw/Medicina/dr prieto medicina interna.pdf` (Manual de Preparación para el ENARM, Curso Dr. Prieto, 14a ed. — extracción dirigida por páginas impresas 6-18, 93-102, 155-166, 167-179, 281-286, 341-350, 388-398, vía subagentes en paralelo, para llenar los vacíos detectados en el MOC de Medicina Interna) | `Cardiopatía Isquémica Crónica (Angina Estable).md`, `Síndrome Coronario Agudo sin Elevación del ST.md`, `Infarto Agudo de Miocardio con Elevación del ST.md`, `Anemias - Generalidades y Clasificación.md`, `Anemia por Deficiencia de Hierro.md`, `Anemia de Enfermedad Crónica.md`, `Anemia Sideroblástica.md`, `Anemia Megaloblástica.md`, `Anemia Aplásica.md`, `Anemia Hemolítica.md`, `Talasemia.md`, `Drepanocitosis.md`, `Esferocitosis Hereditaria.md`, `Deficiencia de G6PD.md`, `Anemia Hemolítica Autoinmune.md`, `Hepatopatía Alcohólica.md`, `Hepatopatía Grasa No Alcohólica.md`, `Hepatitis Autoinmune.md`, `Hemocromatosis Hereditaria.md`, `Enfermedad de Wilson.md`, `Cirrosis Hepática.md`, `Carcinoma Hepatocelular.md`, `Hepatitis Viral.md`, `Hipotiroidismo.md`, `Tirotoxicosis (Hipertiroidismo).md`, `Nódulo Tiroideo.md`, `Cáncer Tiroideo.md`, `Asma.md`, `Enfermedad Pulmonar Obstructiva Crónica (EPOC).md`, `Enfermedad Vascular Cerebral.md`, `Enfermedad Vascular Cerebral Isquémica.md`, `Enfermedad Vascular Cerebral Hemorrágica.md` | `MOC - Medicina Interna.md` |
| 2026-07-08 | `00_raw/Medicina/dr prieto medicina interna.pdf` (sección Ginecología y Obstetricia, páginas impresas ~777-901, sin capa de texto — se extrajo por OCR con Tesseract + modelo en español, vía 6 subagentes en paralelo, a petición explícita de Demian de robustecer Gineco-Obstetricia) | 42 notas nuevas: `Cervicovaginitis - Generalidades.md`, `Enfermedades de la Vulva - Generalidades.md`, `Liquen Plano Vulvar.md`, `Vulvodinia.md`, `Cáncer Vulvar.md`, `Trastornos de las Glándulas Vestibulares Mayores (Bartolinitis).md`, `Enfermedad Pélvica Inflamatoria.md`, `Amenorrea y Oligomenorrea.md`, `Hemorragia Uterina Anormal.md`, `Hiperplasia Endometrial.md`, `Miomatosis Uterina.md`, `Poliposis Endometrial.md`, `Dismenorrea.md`, `Endometriosis.md`, `Adenomiosis.md`, `Síndrome de Ovarios Poliquísticos.md`, `Condiciones Mamarias Benignas.md`, `Cáncer Mamario.md`, `Cáncer Cervicouterino.md`, `Cáncer Endometrial.md`, `Neoplasias Ováricas.md`, `Disfunción Genitourinaria.md`, `Fístula Vesico-vaginal.md` (borrador), `Anticoncepción y Planificación Familiar.md`, `Infertilidad.md`, `Malformaciones Müllerianas Uterinas.md`, `Cambios Fisiológicos del Embarazo.md`, `Diagnóstico y Control del Embarazo.md`, `Trabajo de Parto Normal.md`, `Pruebas de Bienestar Fetal.md`, `Operación Cesárea.md`, `Distocias y Parto Vaginal Instrumentado.md`, `Restricción del Crecimiento Intrauterino.md`, `Puerperio.md`, `Aborto.md`, `Emergencias Obstétricas.md`, `Embarazo Ectópico.md`, `Hemorragia Obstétrica.md`, `Parto Pretérmino.md`, `Ruptura Prematura de Membranas.md`, `Enfermedad Trofoblástica Gestacional.md`, `Embarazo Múltiple.md`, `Isoinmunización al Factor Rh.md`, `Trastornos Hipertensivos del Embarazo.md`, `Muerte Fetal.md`, `Depresión Perinatal (Prenatal y Posparto).md` | `MOC - Gineco-Obstetricia.md`; se ampliaron `Menopausia.md` (+Osteoporosis, contradicción registrada) e `Infección por Virus de la Inmunodeficiencia Humana (VIH).md` (+manejo en el embarazo) |
| 2026-07-09 | `00_raw/Medicina/dr prieto medicina interna.pdf` (sección Pediatría completa, páginas físicas 537-658 / impresas 511-632, sin capa de texto — OCR con Tesseract + modelo en español, vía 13 subagentes en paralelo repartidos en dos rondas por interrupciones de límite de sesión, a petición explícita de Demian de robustecer Pediatría, que solo tenía 16 notas previas) | 58 notas nuevas: `Escalas de Valoración Neonatal.md`, `El Neonato de Término Normal.md`, `Taquipnea Transitoria del Recién Nacido.md`, `Síndrome de Dificultad Respiratoria Neonatal.md`, `Hernias Diafragmáticas Congénitas.md`, `Asfixia Neonatal.md`, `Lesiones Traumáticas de la Cabeza del Recién Nacido.md`, `Lesión Obstétrica del Plexo Braquial.md`, `Retinopatía del Prematuro.md`, `Síndrome Ictérico Neonatal.md`, `Enterocolitis Necrosante.md`, `Síndrome de Aspiración de Meconio (SAM).md`, `Atresia de Vías Biliares.md`, `Atresia Esofágica.md`, `Atresia Intestinal (Duodenal y Yeyunal).md`, `Enfermedad de Hirschsprung.md`, `Malformaciones Anorrectales.md`, `Defectos de la Pared Abdominal (Gastrosquisis y Onfalocele).md`, `Displasia del Desarrollo de la Cadera.md`, `Hipotiroidismo Congénito.md`, `Fenilcetonuria.md`, `Galactosemia.md`, `Fibrosis Quística.md` (borrador), `Enfermedad Hemorrágica del Recién Nacido.md`, `Sepsis Neonatal.md`, `Infecciones Congénitas y Perinatales (TORCH y otras).md`, `Onfalitis.md`, `Desnutrición Infantil.md`, `Lactancia Materna y Sucedáneos de la Leche Materna.md`, `Alimentación Complementaria y Destete.md`, `Crecimiento y Desarrollo Infantil Normal.md`, `Trastornos del Desarrollo Psicomotor.md`, `Esquema Nacional de Vacunación (Cartilla Nacional de Vacunación).md`, `Reflujo Gastroesofágico en Pediatría.md`, `Raquitismo.md`, `Alergia a la Proteína de la Leche de Vaca.md`, `Tumores Malignos en Pediatría - Generalidades.md`, `Tumor de Wilms (Nefroblastoma).md`, `Craneofaringioma.md`, `Neuroblastoma.md`, `Síndrome Hemolítico Urémico.md`, `Mononucleosis Infecciosa.md`, `Amigdalectomía en el Paciente Pediátrico.md`, `Rinosinusitis Aguda.md`, `Otitis Media Aguda.md`, `Otitis Externa.md`, `Epiglotitis (Pediátrica).md`, `Laringotraqueobronquitis (Crup).md`, `Bronquiolitis.md`, `Neumonía Adquirida en la Comunidad (Pediátrica).md`, `Orquitis.md`, `Epididimitis (Pediátrica).md`, `Infección de Vías Urinarias en Pediatría.md`, `Dolor Abdominal Agudo (Pediátrico).md`, `Apendicitis (Pediátrica).md`, `Intususcepción Intestinal.md`, `Divertículo de Meckel.md`, `Aspiración e Ingestión de Cuerpo Extraño.md` | `MOC - Pediatria.md`; se ampliaron `Estenosis Pilórica Hipertrófica.md`, `Infección por Virus de la Inmunodeficiencia Humana (VIH).md`, `Anormalidades del Tracto Urinario y Genital.md`, `Trastornos de la Diferenciación Sexual.md`, `Cardiopatías Congénitas.md`, `Grado de Displasia Renal.md`, `Síndrome de Eisenmenger.md`, `Comunicación Interauricular (CIA).md`, `Persistencia del Conducto Arterioso (PCA).md`, `Transposición de Grandes Vasos (TGV).md`, `Tetralogía de Fallot.md`, `Enfermedades Exantemáticas.md`, `Faringoamigdalitis Bacteriana.md`, `Enfermedad Diarreica Aguda.md`; se detectaron y registraron 3 contradicciones nuevas en `_logs/contradicciones.md` (anticoncepción en Eisenmenger, edad de corrección de PCA, utilidad del ultrasonido en criptorquidia) |
| 2026-07-11 | `DSM-5_espanol.pdf` (extraccion por La Antorcha Humana kimi-k2.6, paginas PDF 172-200, 320-355, 378-400, 641-680) + `00_raw/.../PSIQUIATRIA/TRATAMIENTO PSIQ/` (notas de farmacologia) | `Trastorno Bipolar I.md`, `Trastorno Bipolar II.md`, `Trastorno de Estres Postraumatico.md`, `Trastornos de la Conducta Alimentaria.md`, `Delirium.md`, `Trastorno Neurocognitivo Mayor.md`, `Trastornos Disociativos.md`, `Inhibidores Selectivos de la Recaptura de Serotonina (ISRS).md`, `Benzodiacepinas.md`, `Antidepresivos de Segunda Linea.md`, `Estabilizadores del Estado de Animo.md` | `MOC - Psiquiatria.md` (actualizado); 7 MOCs reconstruidos |
| 2026-07-11 | Auditoria completa de 02_wiki (La Mole GLM-5.2): 201 notas analizadas, 105 notas huerfanas enlazadas, 7 MOCs reconstruidos con enlaces correctos, enlaces rotos reparados | -- | Todos los MOCs |
| 2026-07-13 | Investigación profunda sobre razonamiento clínico (La Mole GLM-5.2, 5 subagentes kimi-k2.6 en paralelo, 46 referencias peer-reviewed) | `Metodo de Estudio Basado en Evidencia para ENARM.md`, `Protocolo Diario de Estudio ENARM.md` | `MOC - Psiquiatria.md`, `00_Inicio.md` |

## 2026-09-07 — Pase de conexión y notas nuevas (La Mole)

- Creada nota wiki [[Síndrome Neuroléptico Maligno]] desde fuente 00_raw; corregido enlace en MOC-Urgencias.
- Creadas 4 notas con fuente curada: [[Gonorrea (Neisseria gonorrhoeae)]], [[Síndrome de Klinefelter]], [[Síndrome de Turner]], [[Virus del Papiloma Humano (VPH)]].
- Pase de conexión: 97 notas huérfanas enlazadas a sus MOC (Cirugía 76, Medicina Interna 17, resto 4). Solo se agregaron enlaces; nada se eliminó.
- 2 archivos de sistema (00_Inicio, ESTADO_PROCESAMIENTO) quedan sin enlace por diseño.
- Enlaces rotos restantes (14): Grupo A (fuentes en Demiank Brain.zip sin extraer), Grupo C (documentos que no están en la bóveda), pendientes de decisión de Demian.

## 2026-09-07 — Puntos 1-3 completados (La Mole)

**Punto 1 — SNM compilado:**
- Creada nota wiki patologias/Síndrome Neuroléptico Maligno.md (síntesis de la fuente 00_raw, con tabla diferencial serotoninérgico y puntos de examen).
- Corregido enlace en MOC-Urgencias (grafía con tilde en "Neuroléptico").

**Punto 2 — 4 notas con fuente curada:**
- patologias/Gonorrea (Neisseria gonorrhoeae).md ← fuente Ginecología/SUBTEMAS
- patologias/Síndrome de Klinefelter.md ← fuente Pediatría/TEMAS SECUNDARIOS
- patologias/Síndrome de Turner.md ← fuente Pediatría/TEMAS SECUNDARIOS
- patologias/Virus del Papiloma Humano (VPH).md ← fuente Ginecología/SUBTEMAS

**Punto 2b — 4 notas en estado borrador sin fuente curada (declarado explícito):**
- patologias/Epiglotitis.md · patologias/Síndrome Serotoninérgico.md ·
  conceptos/Haloperidol.md · conceptos/Vacunas del Esquema Nacional — Descripción Individual.md
  (redactadas de conocimiento estándar GPC; la nota declara "pendiente de fuente curada"
  según la prohibición de la constitución §10).

**Punto 3 — pase de conexión:**
- 97 notas huérfanas enlazadas a sus MOC (Cirugía 76, Medicina Interna 17, resto 4).
- 4 notas nuevas también enlazadas a sus MOC (Pediatría 2, Urgencias 1, Psiquiatría 1).
- Solo se agregaron enlaces; nada eliminado. 00_Inicio y ESTADO_PROCESAMIENTO quedan sin
  enlace por diseño (archivos de sistema).

**ESTADO FINAL VERIFICADO:** 320 notas · 0 huérfanas · 0 enlaces rotos reales
(restan 14 wikilinks del Grupo A/C pendientes de la decisión del zip Demiank Brain
 y de ubicar documentos de estudio; las referencias de frontmatter "fuentes:" a 00_raw
 son válidas por diseño de la constitución).

## 2026-09-07 — Estructura de registro de errores por especialidad (pedido de Demian)

- Skill refuerzo-examenes-enarm actualizado (sección 0): cada especialidad tendrá 3 carpetas
  internas — 01_preguntas (transcripción + caso + respuesta correcta, grupos compartidos
  juntos, archivos de ~100), 02_resumenes (material didáctico del profesor por temas de 10),
  03_analisis (por qué me equivoqué + técnica T1-T13 + plan de mejora).
- Convención documentada en registro_errores_enarm/README_ESTRUCTURA.md.
- Los 7 MOC de 02_wiki/indices/ ahora enlazan a la carpeta de registro de su especialidad.

## 2026-09-08 — Paquete TAP (terapia asistida con perros) completado

- 3 protocolos con estructura canónica A-1 (carta 10 filas + mapa 3 bandas + algoritmo):
  TAP-01 Higiene de manos (5 momentos OMS adaptados al programa) ·
  TAP-02 Miasis gusano barrenador caninos/felinos (SENASICA/CNMVB) ·
  TAP-03 Miasis en humanos (Manual CONAVE 2025 como fuente primaria, SINAVE/RNLSP).
- 3 algoritmos .drawio (XML válido, rombos SÍ/NO, 0 huérfanas) + 3 JPG.
- Word de 3-4 páginas con algoritmo incrustado en 14x21.2cm.
- Fuente real del usuario subida a Drive (TAP/): manual CONAVE 2025, NOM-017, programa,
  consentimiento, tarjetón PC-TAP-F11. Supuestos reducidos a los mínimos.
- Ubicación: ~/Documents/MOCEPBASS/TAP/ + ENARM_Cerebro_Demiank/mocepbass_entregables_tap/.
- Versión v0.2 (borrador sin validación de jefatura — regla 18 del skill).

## 2026-09-08 — Skills v2 instaladas (paquete del usuario)

- Respaldo previo: ~/.hermes/skills_respaldo_2026-09-08/
- Instaladas: protocolo-razonamiento (nuevo, v1.0) + 7 SKILL.md v2 (mocepbass-hsmo,
  egreso-hospitalario, clinical-document-generation, enarm-material-compilation,
  refuerzo-examenes-enarm, demiank-cerebro-enarm, second-brain)
- ESTADO_PROYECTO.md instalado en ~/Documents/MOCEPBASS/ (A-13a21 renombrados v0.3,
  TAP v0.2 pendiente de corrección v0.3)
- lecciones.md instalado en enarm-study-trainer/references/
- Revisión técnica TAP copiada a mocepbass-hsmo/references/
- Pendiente por recibir: html-typing-app-builder v2, los-4-fantasticos v2,
  enarm-study-trainer v2 (SKILL.md), iseo-deep-research v2 (o confirmar sin cambios)
- Pendiente README §4: pegar contenido del protocolo en la personalidad global
  (requiere decisión del usuario o revisión de config.yaml)

## 2026-09-08 (noche) — Paquete skills v2 COMPLETO instalado desde Drive (gdrive:v2)

- 30 archivos descargados y analizados; 17 instalados nuevos + 12 ya idénticos + 4 actualizados.
- 12 skills v2 + protocolo-razonamiento v1.0 verificados en disco con name/version.
- A13-A21 renombrados v1.0→v0.3 (9 archivos, local + Drive) y versión interna de cada
  .docx sustituida (4 run por archivo) con los scripts ESTADO del paquete.
- ESTADO_PROYECTO.md vigente en ~/Documents/MOCEPBASS/ (única fuente de verdad).
- Respaldo previo: ~/.hermes/skills_respaldo_2026-09-08/
- Pendiente: fecha del ENARM (fecha_enarm.txt vacío) y corrección v0.3 del paquete TAP.

## 2026-09-08 (noche 2) — verificación completa de v2 vs Drive y ajustes

- gdrive:v2 descargado y comparado bit a bit: 29/30 idénticos a lo instalado;
  README_CAMBIOS.md copiado a ~/.hermes/skills/ para referencia.
- Ajustes en los-4-fantasticos: perfiles (solo default existe; antorcha/invisible son
  binarios en ~/.local/bin, se activan via delegate) y kanban boards reales (default, enarm).
- HALLAZGO OPERATIVO: el cron del entrenador ENARM (5AM/6PM) NO está registrado;
  solo existe Alerta Batería. entrenador-entrega.sh existe pero sin job que lo dispare.
- Análisis completo en _procesamiento/analisis_skills_v2.md

## 2026-09-08 (noche 3) — decisión del usuario sobre crons del entrenador

- El usuario decidió NO registrar los cron jobs 5AM/6PM del entrenador ENARM:
  la entrega de entrenamientos queda MANUAL (Demian los pide cuando los quiere).
- El script entrenador-entrega.sh permanece en ~/.hermes/scripts/ disponible para
  registro futuro si cambia de opinión.

## 2026-09-08 (noche 4) — cierre del paquete TAP por decisión del usuario

- El usuario informó que ajustó los 3 protocolos TAP con Claude ("Así déjalo ya lo
  ajuste con claude") y ordenó dejar el trabajo como está: NO se ejecuta la v0.3
  por La Mole.
- Estado que queda en disco local (mocepbass_entregables_tap/): 3 docx v0.2 +
  3 JPG + .drawio + script generador, sincronizados en gdrive:FORMATOS MOCEPBASS/TAP/.
- Las 12 reglas permanentes (29-37) de la revisión técnica permanecen en la skill
  mocepbass-hsmo para futuros entregables del proyecto.
- Ubicación de la corrección de Claude: por confirmar si sube los ajustados a Drive.
