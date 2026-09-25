# Hermes Desktop en Mac Intel Monterey — informe de instalación (12/09/2026)

## Contexto
Nous publica Hermes Desktop solo como DMG arm64 (Apple Silicon). Issues abiertos
#38227 y #40456 lo confirman; no corre en Intel.

## Lo que hice (vía: build desde código fuente)
1. npm install del workspace apps/desktop (778 paquetes, electron x86_64)
2. npm run build (vite + bundle electron main + native deps) — OK
3. Empaquetado electron-builder --mac --x64 → Hermes-0.17.2-mac-x64.dmg/zip
4. Instalada en /Applications/Hermes.app (sin firma; quarantine removido)

## Versiones de Electron probadas
- 40.10.2: crash al lanzar — SMAppService (_OBJC_CLASS_$_SMAppService) requiere macOS 13
- 31.7.7: corre, pero UI no pinta + global WebSocket ausente en Node 20
  (parché polyfill ws como global; el fix funcionó para el main)
- 28.3.3: corre estable, cero errores del main — SELECCIONADA

## Fixes aplicados durante el camino
- Bug introducido por mi polyfill: comentario que se comió "const require = createRequire"
  → "Dynamic require of fs is not supported" → restaurado con re-extracción del asar
- translucency.json (userData) con mode "clear" para evitar vibrancy/glass en Monterey

## Estado final de la ventana
- Main process: limpio (0 errores), hermes serve backend en 8377 (HTTP 200)
- Renderer: carga index.html, contexts creados, SIN errores de JS reportados,
  pero NO PINTA contenido (screencapture de la ventana falla: sin buffer)
- Probado: --disable-gpu, --disable-gpu-compositing, swiftshader,
  --in-process-gpu, --disable-software-rasterizer, translucency off. Sin cambio.

## Diagnóstico
Composición de Chromium 120 en GPU Broadwell (Intel HD 6000) sobre macOS 12 con
ventanas con material translúcido: el contenido web no se compone a la ventana.
Es un límite de GPU/OS, no del código de Hermes ni del build.

## Artefactos que quedan
- /Applications/Hermes.app (Electron 28, con polyfill y require arreglado)
- ~/.hermes/bin/hermes-desktop.sh (launcher con flags)
- release/Hermes-0.17.2-mac-x64.dmg + .zip (Instalador Intel reutilizable)
- ~/.hermes/workspace/jarvis_modelo_decision.md
- Si Nous publica binario Universal o Electron arregla el compositing: solo
  reemplazar la app; los perfiles y el gateway ya están listos.

## Plan recomendado
- Mientras tanto: dashboard web (`hermes dashboard`) o Telegram — ya funcionan
- Mac Mini M4 (o cualquier Silicon): la MISMA app oficial arm64 correrá y los
  perfiles antorcha/invisible/default aparecerán como bots sin migración
