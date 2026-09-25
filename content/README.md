# ENARM Cerebro Demiank — Guía de uso

Bóveda de Obsidian construida bajo el patrón "LLM Wiki" (Karpathy, 2026): las fuentes originales se conservan intactas, y un modelo de lenguaje (Claude, vía Cowork o Claude Code) mantiene una wiki interconectada a partir de ellas.

## 1. Estructura de la bóveda

```
ENARM CEREBRO DEMIANK/
├── CLAUDE.md              ← Reglas del sistema (léelo antes de pedir procesamiento)
├── README.md              ← Este archivo
├── 00_raw/                ← Capa 1: fuentes originales, INTOCABLES por la IA
│   ├── GPC/
│   ├── DSM-5/
│   ├── articulos/
│   ├── notas_clase/
│   ├── casos_clinicos/
│   └── ENARM_reactivos/
├── 01_inbox/               ← Bandeja de entrada para material sin clasificar aún
├── 02_wiki/                ← Capa 2: wiki generada y mantenida por la IA
│   ├── 00_Inicio.md         ← Dashboard / nota de inicio
│   ├── conceptos/
│   ├── patologias/
│   ├── farmacologia/
│   ├── casos_clinicos/
│   └── indices/             ← Mapas de contenido (MOC) por especialidad ENARM
├── _templates/              ← Plantillas de nota (concepto, patología, fármaco, caso clínico, MOC)
└── _logs/                   ← Bitácora de procesamiento y registro de contradicciones
```

## 2. Abrir la bóveda en Obsidian

1. Abre Obsidian.
2. "Abrir carpeta como bóveda" → selecciona `ENARM CEREBRO DEMIANK`.
3. En Ajustes → Nota de inicio, selecciona `02_wiki/00_Inicio.md` para que sea la pantalla de arranque.
4. (Opcional) Instala el plugin comunitario "Templater" para usar las plantillas de `_templates/` con variables automáticas de fecha y título.

## 3. Cómo depositar fuentes

- PDFs de GPC, capítulos del DSM-5, artículos científicos, apuntes de clase, reactivos de práctica ENARM: cópialos directamente a la subcarpeta correspondiente de `00_raw/`.
- Si no tienes tiempo de clasificar algo en el momento, déjalo en `01_inbox/` y se procesará desde ahí.
- Nunca edites manualmente el contenido de `02_wiki/` sin necesidad: es territorio de la IA. Si quieres anotar algo tuyo, hazlo en un bloque de comentario o pídele a la IA que lo incorpore.

## 4. Cómo pedir el procesamiento

Este sistema no corre en automático de fondo: tú decides cuándo procesar. Tienes dos formas de operarlo, ambas usan las mismas reglas de `CLAUDE.md`:

**Opción A — Cowork (esta misma conversación o una nueva)**
Con la carpeta `ENARM CEREBRO DEMIANK` conectada, simplemente pide: *"procesa las fuentes nuevas de 00_raw"* o *"revisa el inbox y actualiza la wiki"*. Claude leerá `CLAUDE.md`, procesará lo pendiente y escribirá directamente en `02_wiki/` y `_logs/`.

**Opción B — Claude Code (terminal, en tu equipo con Bazzite/Linux)**
Si más adelante quieres automatización tipo comandos (`/ingest-url`, `/process-inbox`, `/lint-wiki`), instala Claude Code, sitúate en la carpeta de la bóveda y trabaja desde la terminal. Claude Code leerá el mismo `CLAUDE.md` como su archivo de configuración raíz.

Ambas opciones son intercambiables porque comparten la misma "constitución" (`CLAUDE.md`) y la misma estructura de archivos.

## 5. Auditoría periódica

De vez en cuando pide: *"audita la wiki"* o *"haz un lint de la bóveda"*. Se revisarán enlaces rotos, notas huérfanas, vacíos de temario ENARM y notas en borrador olvidadas (ver sección 9 de `CLAUDE.md`).

## 6. Repaso previo al examen

Usa los MOC de `02_wiki/indices/` como guion de repaso por especialidad. Cada MOC lista conceptos, patologías, fármacos y casos clínicos enlazados, además de los vacíos de contenido detectados que conviene reforzar antes del ENARM.
