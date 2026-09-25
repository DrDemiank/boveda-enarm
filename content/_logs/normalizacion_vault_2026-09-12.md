# Normalización de la bóveda — 12/09/2026

## Ejecución
- 10 subagentes en paralelo (glm-5.3-flash) corrigieron 330 enlaces rotos en 305 notas.
- Verificación independiente del orquestador tras cada lote.

## Inventario inicial (audit_wiki.py NFC)
- 320 notas; 329 enlaces rotos; 104 nombres NFD; 2 huérfanas por diseño; 13 borradores.

## Hallazgos técnicos
1. Los nombres NFD no requieren renombrado: APFS normaliza NFC≈NFD al comparar
   (renombrar produce colisión de sí mismo). El único efecto es en comparaciones
   byte-a-byte de scripts Python; el auditor ya compara con NFC.
2. 309 de 330 rotos eran enlaces [[...]] hacia fuentes raw (00_raw) — convertidos
   a texto plano "fuente: X" (la constitución los pide como fuente, no como wikilink).
3. 8 rotos eran enlaces internos mal escritos (Turner, Klinefelter, SNM, Gonorrea)
   o anchors — corregidos al nombre exacto de la nota real.
4. El reemplazo literal dentro de `fuentes: ["[[X]]"]` producía YAML inválido
   (`""fuente: X""`). Corregido en 181 notas con regex determinista:
   `""(fuente: [^"]*)""` → `""`. Validación final: 320/320 YAML válido.
5. Anchos internos [[#Sección|alias]] causaban falso "enlace roto" en el auditor
   (target tras split("#") queda vacío). Patch en audit_wiki.py: los anchors internos
   marcan la nota como referenciada y no se evalúan como target externo.

## Estado final (audit_wiki.py, verificado en vivo)
- Notas: 320 (patologias 256, conceptos 27, banco_preguntas 23, indices 7, farmacologia 6, raíz 1)
- Enlaces rotos REALES: 0 (antes 329)
- Duplicados NFC/NFD: 0
- Sin frontmatter: 0
- Notas < 500 bytes: 0
- Huérfanas: 2 (00_Inicio.md, ESTADO_PROCESAMIENTO.md — por diseño, no se tocan)
- Borradores: 13 (trabajo clínico pendiente, no defecto de normalización)

## Pendiente de otra sesión
- 13 borradores requieren fuentes curadas (trabajo clínico, no mecánico).
- Sincronizar 02_wiki a Drive (rclone).

## Extension: eficiencia de busqueda (mismo dia, sesion 2)

Analisis de los 7 MOCs y ajustes aplicados (scripts deterministas, sin LLM):
1. Especialidades del frontmatter normalizadas a taxonomia canonica ENARM en 102
   notas (GinecoObstetricia->Gineco-Obstetricia, Medicina_Interna->Medicina Interna,
   Salud_Publica->Salud Publica).
2. 7 MOCs regenerados con estructura canonica (secciones unicas, sin duplicados;
   incluidas las 4 notas que no estaban: Klinefelter, Turner, Gonorrea, VPH).
3. Indice Maestro.md creado: catalogo A-Z de las 320 notas + agrupacion por
   especialidad (el acelerador principal de busqueda).
4. Alias de Busqueda.json creado: 38 abreviaturas/sinonimos (SNM, TDM, TAG, TOC,
   TEPT, ISRS, TCA, ECT, HTA, EPOC, TCE, TGV, PCA, HUS, RCIU, TVP, ERC, etc.)
   mapeados a nombres exactos de notas (verificados por NFC).
5. Auditoria final: 321 notas, 0 rotos, 0 duplicados, 0 YAML invalido.

## Uso con La Mole
Para pedir un tema: nombre exacto, abreviatura o sinonimo (el alias lo resuelve);
la busqueda es inmediata via Indice Maestro.md + Alias de Busqueda.json.

## Flashcards ENARM por patologia (12/09/2026, sesion 3)

10 subagentes GLM 5.3-flash generaron 1578 flashcards para 285 patologias
(4-6 tarjetas por patologia: criterio diagnostico, primera linea, farmaco+dosis,
hallazgo de lab/imagen, complicacion aguda; reverso con dato diferencial).
Fuentes: notas 02_wiki + patrones de las 529 preguntas del banco. Anti-invencion:
dosis/criterios solo de nota o banco; notas borrador limitadas a su contenido.

Entregables: 6 PDF por especialidad en flashcards_enarm/ (Psiquiatria 87, Medicina
Interna 225, Cirugia 489, Pediatria 374, Gineco-Obstetricia 265, Urgencias+SP 138)
+ .md fuente. Sincronizado a Drive.

## Recabacion @PuntoENARM (13/09/2026, sesion 4)

Mision: guardar las tarjetas numeradas N/3000 de @PuntoENARM (X) del ultimo ano.
Herramienta: twifork 2.4.0 (fork mantenido de twikit, encontrado en internet)
+ cookies de sesion del Chrome del agente (CDP). Paginacion real 20/req con
cursor; esquiva 429 con 30s entre paginas. Barrido en 3 tandas (~44 paginas).

RESULTADO: 794 tarjetas unicas N343 (16 feb 2026) -> N1140 (12 sept 2026).
La cuenta empezo a numerar en feb 2026: no existen tarjetas anteriores (el
"ano pasado" de tarjetas N no existe; antes habia hilos y material suelto).
4 huecos: N1111-1114 (eliminados por la cuenta). Guardado en
02_wiki/banco_preguntas/PuntoENARM - Tarjetas 2026.md (84 KB, agrupado por mes)
+ sincronizado a Drive.

## Clasificacion y distribucion de las 794 tarjetas (13/09/2026, sesion 5)

10 subagentes GLM clasificaron las 794 tarjetas de @PuntoENARM (lotes 6 y 9
reintentados tras 429). Resultado: 467 ligadas a nota del vault, 327 pendientes
(sin nota). Distribucion: Medicina Interna 242, Cirugia 234, Pediatria 138,
Urgencias 93, Gineco-Obstetricia 77, Salud Publica 8, Psiquiatria 2.

Entregables:
1. 7 .md por especialidad en flashcards_enarm/ + PuntoENARM_Temas_Pendientes_Sin_Nota.md
2. Seccion "## Preguntas PuntoENARM" insertada en 190 notas del vault (467
   tarjetas enlazadas con numero, fecha y wikilink)
3. PDFs por especialidad (generacion en curso; los 5 chicos listos)
4. Vault integro: 322 notas, 0 rotos, 0 duplicados, Drive sincronizado.
