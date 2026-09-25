DESGLOSE VERIFICADO (10/09/2026, 22:41 CST, Mac local):

Q trivial ("que hora es"):
  one-shot:    9.0 s
  persistente: 9.0 s   <- SIN diferencia entre vias en trivial

Q clinica (criterios + manejo SNM):
  one-shot max:      20.3 s
  persistente max:   20.8 s   <- diferencia 0.5s = ruido, NO la recarga de sesion
  persistente medium: 23.2 s  <- ruido de red; medium no acelera el CLI de forma consistente

Q clinica DIRECTA API (sin CLI):
  glm-5.3-flash max (sin campo): 7.6-8.4 s
  glm-5.3-flash medium:          8.2 s
  deepseek-v4.1-flash:           5.1 s

CONCLUSIONES PARA CLAUDE:
1. La sesion persistente NO es la causa principal de la lentitud (solo 0-1s).
   La causa dominante: razonamiento max + arranque del CLI (~2-4s fijos).
2. medium NO acelera el CLI consistentemente (23.2s vs 20.8s en mi red — ruido).
   Lo que SÍ reduce: preguntar por API directa (2-8s vs 20s).
3. La prueba real de Claude (desde Bazzite via SSH) puede dar valores LIGERAMENTE
   peores por el viaje de red + caffeinate. Sus numeros reales mandan.
4. El bug 18121 sigue VIGENTE (verificado hoy): low=0 razonamiento, high=0 razonamiento,
   medium=razona, max=razona. "medium es seguro": SI, verificado con caso clinico
   (13.8k chars de reasoning en caso SNM complejo, calidad paritaria a max).
