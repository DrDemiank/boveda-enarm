# Bazzite Desktop — diagnóstico final (12/09/2026)

## Por qué la UI no pinta texto en Bazzite
La captura del doctor muestra Chromium sin fuentes: "Could not find any font:
Noto Sans, sans" (platform_font_skia.cc) + NOTREACHED en remote_font_face_source.
Las fuentes web del bundle fallan y el fallback del sistema no resuelve en el
entorno del AppImage. Bazzite base no trae Noto Sans en la imagen.

## Fix (1 línea, cuando se quiera retomar)
rpm-ostree install google-noto-sans-fonts google-noto-sans-mono-fonts && systemctl reboot

## Estado del circuito igualmente logrado
- AppImage construida en Bazzite desde source (Electron funcionando)
- Conexión SSH Bazzite→Mac OK (llave autorizada, CONEXION_OK)
- connections.json v2 pre-registrado (schema extraído del source)
- Serve de la Mac como LaunchAgent (8377) + web_dist compilado
- hermes/node en PATH global de la Mac (/usr/local/bin)

## Subagentes
- Límite: 10 en paralelo (delegation.max_concurrent_children default)
- Modelo: kimi-k3 (delegation.model) — compartible con overrides por tarea
- Casos de uso acordados con el doctor: ver conversación 12/09