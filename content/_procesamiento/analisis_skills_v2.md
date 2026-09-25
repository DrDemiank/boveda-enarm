
ANÁLISIS DE LA CARPETA v2 (Drive) — 30/30 archivos instalados y verificados bit a bit

═══ LO QUE ESTÁ BIEN Y FUNCIONA ═══
1. protocolo-razonamiento v1.0 — sólido, coherente, instalado y cargable. Es la mejora
   estructural más importante del paquete (anti-invención, presupuesto, cotejo).
2. mocepbass-hsmo v2.0 — contradicciones del v1 resueltas (14 nodos, mapa 8 campos,
   plantilla IXA-01, versionado sin excepciones). Estado movido a ESTADO_PROYECTO.md.
   Los 2 scripts de ESTADO funcionaron: A13-A21 renombrados v0.3 y versión interna actualizada.
3. egreso-hospitalario v2.0 — flujo de una pasada consolidado, prevalece sobre clinical-document.
4. enarm-study-trainer v2.0 + lecciones.md — sincronía con refuerzo (temas 2+ fallos).
5. demiank-cerebro-enarm v2.0 + audit_wiki.py con NFC — corrección del falso 693 rotos.
6. enarm-material-compilation v2.0 — bitácora de 70 KB fuera del contexto (era el problema #1).
7. html-typing-app-builder v2.0 — historial de funciones a references.
8. refuerzo-examenes-enarm v2.0 — delegación de manuscritos (3 automáticas) + fecha ENARM.
9. second-brain v2.0 — solo mapa de modos (4 KB).
10. iseo-deep-research v2.0 — sin cambios de fondo, correcto.

═══ INCONSISTENCIAS MENORES DETECTADAS (vs realidad del sistema) ═══
1. los-4-fantasticos dice que hay perfiles "default/antorcha/invisible" — el sistema solo
   tiene el profile default vacío y los comandos antorcha/invisible son launchers que NO
   existen como perfiles hermes formales (antorcha es un script binario en ~/.local/bin).
   → Ajuste: la skill debe decir "los perfiles antorcha/invisible se activan via delegate;
   no existen como perfiles hermes permanentes en esta instalación".
2. Kanban: la skill dice boards "hospital, enarm, proyectos" — la realidad: "default, enarm".
   → Ajuste menor: actualizar nombres de boards.
3. Cron: la skill describe el patrón script-only correctamente (existe: Alerta Batería).
   El cron de entrenador 5AM/6PM NO está activo hoy en hermes cron list — solo el de batería.
   → Verificar con el usuario: ¿los crons del entrenador se movieron a LaunchAgent
   (com.hermes.enarm-drive-sync existe para Drive) o el cron ENARM está pausado?
4. Fallbacks: config.yaml NO define fallback_providers — la skill lo maneja bien (reportar
   error literal y detenerse). Sin acción necesaria.

═══ AJUSTES APLICADOS YA ═══
- .hermes.md actualizado: modelo correcto (glm-5.3-flash), protocolo de razonamiento
  referenciado, ESTADO_PROYECTO como fuente de verdad.
- README_CAMBIOS.md guardado en ~/.hermes/skills/ para referencia.


═══ HALLAZGO OPERATIVO (08/09/2026 noche) ═══
El cron del entrenador ENARM (5AM/6PM) NO está registrado en hermes cron list:
solo existe "Alerta Batería Mac". El script entrenador-entrega.sh sí existe en
~/.hermes/scripts/ y funciona en modo script-only, pero sin job que lo dispare.
→ DECIDIDO por el usuario (08/09/2026): NO registrar crons del entrenador.
  La entrega de entrenamientos queda MANUAL. El script queda disponible si cambia de opinión.
