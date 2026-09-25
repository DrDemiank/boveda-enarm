# Claude sin API en Hermes — riesgo de ban (investigación 11/09/2026)

## Dos cosas distintas
A) PR #98533 (NousResearch, ABIERTO no fusionado): provider claude-code-cli oficial,
   setup-token, dentro de términos. Es la vía sana futura.
B) Bypass comunitario "hermes-claude-auth" (388 est.): anthropic_billing_bypass.py
   suplanta al CLI oficial ante Anthropic (headers facturación firmados + spoof SDK
   Stainless + reescritura de prompts para pasar validación del 04/04/2026).
   Auto-repara tras cada update (git hooks + cron cada 15 min).

## Riesgo de ban: SÍ, CONCRETO
- Anthropic endureció filtros contra spoofing del harness (Thariq Shihipar, Staff Eng)
- El rollout de abril baneó automáticamente cuentas inocentes (colateral admitido)
- OpenCode bloqueado por replicar OAuth; lanzó tier enterprise de pago
- Suscripción Pro/Max = solo CLI oficial; fuera de Claude Code NO permitido
- README del bypass: "Use at your own risk"

## Recomendación: NO instalar el bypass
Vías sanas: PR #98533 cuando se fusione, API key de pago, o seguir en Ollama Pro
(~$0.15/mes, capacidad comparable). Fuente completa en este archivo.


## ANEXO: ChatGPT/Codex es DIFERENTE (verificado 11/09)
- Hermes usa el client_id OFICIAL de Codex: "app_EMoamEEZ73f0CkXaXp7hrann"
  (mismo string que pub const CLIENT_ID en openai/codex codex-rs/login/src/auth/manager.rs:1724)
- Endpoint oficial auth.openai.com + device-code login → flujo oficial de OpenAI
- La ayuda oficial de OpenAI documenta "Sign in with your ChatGPT account" para Codex
- NO hay suplantación, NO hay bypass → riesgo bajo (sujeto a límites del plan)
- Disponible HOY en Hermes: hermes auth -> openai-codex; integrado en Desktop
