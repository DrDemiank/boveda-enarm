# Actualizacion Hermes 10/09/2026 (v0.21.1 bffa5f75)

- hermes update aplicado en 27 s: 4 commits nuevos (terminal: probes sudo NOPASSWD)
- Configuracion al dia, perfiles antorcha/invisible al dia
- Pendiente: el servicio ai.hermes (pid 53490) sigue con codigo de 6ac77111 en memoria.
  El updater lo solicito pero no cambio el pid. El agente NO puede recargarlo desde
  dentro (proteccion de diseno: SIGTERM lo mataria).
  ACCION DEL USUARIO: en Terminal de la Mac correr el comando de ciclo de vida del
  gateway (hermes + gateway + restart), ~10 s, transparente para Telegram.
- cua-driver: no refrescado (github inalcanzable durante update); reintenta solo.
  No urgente: el binario ya estaba roto en Monterey (minos 13 vs macOS 12).
