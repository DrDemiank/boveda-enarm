# Capacidad completa en la Mac (10/09/2026) — restauración de limitantes

## Hardware y sistema
MacBook Retina 12" Early 2015 (MacBook8,1), Intel i5-5250U 1.6GHz, 8GB RAM, 17Gi disco libre,
macOS 12.7.6 Monterey (ultima version oficial). Electron: Intel x86_64.

## Componentes RESTAURADOS hoy (sin cambiar macOS)
1. browser-use CLI 0.1.13: instalado en ~/.hermes/bin/browser-use (via tools.browser_use_cli.install_cli)
2. Chrome CDP propio: ~/.hermes/bin/hermes-chrome-cdp.sh (headless, puerto 9222, perfil
   ~/.hermes/chrome-cdp-profile, NO toca el Chrome del usuario)
3. Vigilante permanente: LaunchAgent ai.hermes.chrome-cdp (revive Chrome CDP si muere,
   chequeo cada 30s; log ~/.hermes/logs/chrome-cdp.log)
4. browser.cdp_url = http://127.0.0.1:9222 en config.yaml -> browser_exec FUNCIONA
   (verificado: goto_url + js + page_info contra example.com y ollama.com/library)
5. pyautogui 0.9.54 en venv Hermes (screenshot 1440x900 OK; control mouse/teclado)
6. cliclick 5.1 compilado del source -> ~/.hermes/bin/cliclick (click/teclado real OK)
7. cua-driver 0.11.0 instalado (importa OK; binario upstream NO funciona en Monterey
   por Foundation macOS 13+ — cobertura via pyautogui+cliclick+screencapture)
8. faster-whisper 1.2.1 + ctranslate2 4.8.2 (CPU) — STT local OK (tiny 2.9s/2s audio)
9. npm actualizado a 11.17.0 (~/.npm-global/bin en PATH de bash_profile)
10. Vulnerabilidades npm: raiz 0; web solo 3 moderadas en dev-deps (limpiarlas con
    --force rompe builds: NO se hace; se limpian con el lockfile upstream)

## Lo que sigue SIN solucion sin OCLP
- computer_use tool de Hermes (cua-driver binario) — IRRECUPERABLE en Monterey:
  binario compilado contra macOS 13+ SDK. Alternativa: pyautogui/cliclick (equivalente).
- Hermes Desktop app Electron: funciona en macOS 12? no verificado (no es prioridad).

## Vía "actualización no oficial" (OCLP) — DISPONIBLE pero NO ejecutada
OpenCore Legacy Patcher lista a MacBook8,1 como soportada ("Legacy Metal macOS 13+").
Puede llevar la máquina a Sequoia (15)/Tahoe (26) con Metal parcheado.
REQUISITOS: ~35-40Gi libres en disco (hay 17Gi: INSUFICIENTE) y respaldo completo.
GANANCIA si se hace: computer_use nativo + APIs nuevas + desktop moderno.
RIESGO: Core M 1.6GHz + 8GB en Sequoia es MUY justo; Metal "legacy" puede dar
problemas de estabilidad gráfica; OCLP rompe actualizaciones OTA de macOS.
DECISION: NO ejecutado. La Mac YA tiene todas las funciones de Hermes operativas
(browser real, STT, control de escritorio, crons, gateway) sin OCLP. OCLP solo
agregaria el tool computer_use nativo, que ya tiene doble respaldo (pyautogui/cliclick).
