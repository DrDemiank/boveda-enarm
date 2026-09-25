# Jarvis — latencias medidas (08/09/2026)

A. hermes CLI por SSH: max ~18s | medium 9.4-10.4s | sesion continua 27-39s
   (arranque CLI + skills + contexto = costo fijo 2-4s sobre la API)

B. API directa Ollama Cloud (sin CLI):
   glm-5.3-flash: 2.5s trivial / 7.6s clinica (sin effort) / 5.3-8.2s medium
   deepseek-v4.1-flash: 5.1s clinica (respuesta correcta)
   20 modelos disponibles en la API (lista en esta misma carpeta)

Conclusion: via mas rapida = API directa (2-8s). Router hibrido en jarvis.py:
- conversacion/despacho -> API directa (5s)
- clinico/skills -> hermes CLI (9-18s)
- patron de respuesta en dos tiempos: respuesta rapida + confirmacion detallada
