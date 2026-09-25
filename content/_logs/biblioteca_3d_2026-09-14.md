# Bitácora — Biblioteca Virtual 3D (13-14/09/2026)

## Opción A — Biblioteca interactiva (ENTREGADA)
- Archivo: biblioteca-virtual-v1.html (796 KB, JS validado con node --check)
- Estantería de código: 4 estantes, ~70 libros/estante (12 reales del catálogo + 280 ambiente)
- Panel de lectura al hacer clic (verificado en vivo: fondo crema, título, autor, botón)
- Buscador por título/autor, caminar WASD + ratón pointer lock
- CAPA ESCANEO REAL: botón toggle que carga nube de puntos GLB (parse manual,
  pc.Mesh + StandardMaterial vertexColors + diffuseVertexColor)
- Lecciones técnicas:
  - PlayCanvas 2.9: NO existe pc.BasicMaterial (StandardMaterial con
    useLighting=false + diffuseVertexColor es la vía para puntos con color)
  - MeshInstance firma 2.9: (mesh, material, graphNode) — NO (node, mesh, mat)
  - mesh.incRefCount error = orden de args al revés
  - Podman rootless + SELinux en Bazzite: bind mounts del home necesitan :Z
    y aun así SQLite falla con "disk I/O error" — usar VOLUMEN nombrado de podman
  - colmap/colmap:latest es CUDA-only; graffitytech/colmap:3.8-cpu-ubuntu22.04
    es la imagen CPU que funciona
  - colmap model_converter: bin->TXT necesario para OpenMVS InterfaceCOLMAP
  - GLB de puntos: mode 0 (POINTS), COLOR_0 uint8 normalized, parse manual
    del chunk JSON + BIN (sin librería, decodificación propia en JS)

## Opción B — Fotogrametría real (EN CURSO en la Bazzite)
- 63 imágenes (31 fotos + 32 frames video) subidas por SSH a
  /var/home/Demiank/biblioteca_prueba (volumen podman datos-biblio)
- Pipeline COLMAP CPU completado:
  1. feature_extractor: 126 archivos, 0.8 min ✓
  2. exhaustive_matcher: 9.6 min, 1531% CPU ✓
  3. mapper: modelo 0 con 122/126 imágenes registradas ✓
  4. model_converter -> modelo.ply (61,139 puntos RGB) ✓ descargado a Mac
  5. GLB sparse generado (563 KB recortado, 38,409 puntos) e incrustado ✓
  6. image_undistorter: terminado ✓ (124 imágenes)
- OpenMVS en marcha: InterfaceCOLMAP con crash _Map_base::at pendiente de
  resolver (nombres frame_030.jpg vs IMG_*.jpg en undistorted)
- DensifyPointCloud CPU: 4-10 h estimado cuando arranque

## Estado del archivo entregado
- HTML con estantería de código + capa escaneo sparse real (toggle)
- El dense reemplazará la nube cuando termine (mismo toggle)


## CIERRE NOCTURNO (02:30, 14/09) — Bazzite por apagar
- El doctor necesita apagar la Bazzite → estrategia de traslado:
  1. La cadena nocturna COMPLETÓ antes del apagado: ReconstructMesh rc=0
     (malla 5.5M vértices / 10.7M caras, 204 MB), TextureMesh rc=0 en 0s
     (falló silenciosamente — scene_dense_mesh.mvs no existía, produce .ply),
     export_scene_mvs no existe en la imagen (binarios solo en /usr/local/bin/OpenMVS/)
  2. DESCARGADO A LA MAC (seguro):
     - scene_dense.ply (719 MB, nube densa)
     - scene_dense_mesh.ply (204 MB, malla densa 5.5M verts / 10.7M caras)
     - scene.mvs (cámaras 4.7 MB)
  3. GLB denso generado: 1.2M puntos de la superficie de la malla, 17 MB,
     incrustado en biblioteca-virtual-v1.html (22 MB) — verificado en vivo:
     la sala se ve SÓLIDA (paredes, piso, estantería continua)
  4. Cron re-programado (job 17a47ddd05c4, 12:22 pm): texturizado mañana
     — necesita Bazzite encendida (TextureMesh sobre scene_dense.mvs con
     --mesh-file scene_dense_mesh.ply) → OBJ+MTL+texturas → GLB decimado
     → sustitución en el HTML → entrega final
- La Bazzite puede apagarse: nada se pierde, la geometría está en la Mac.
- Pendiente único: la TEXTURA (mañana, ~10 min de cómputo en la Bazzite).


## PLAN STACK IA LOCAL BAZZITE (14/09, 03:55)
Investigación completa (subagente GLM, 51 min, fuentes oficiales):
- Plan: ~/.hermes/workspace/contexto-claude/PLAN_STACK_LOCAL_BAZZITE_RX9070XT.md (v0.1)
- Scripts listos: instalar_ia_local_bazzite.sh + descargar_modelos_bazzite.sh (sintaxis verificada)
- Arquitectura: Ollama ROCm en podman Quadlet (RDNA4 requiere ROCm 7.x, solo Ubuntu/RHEL — la imagen ollama/ollama:rocm lo trae; NO HSA_OVERRIDE para gfx1201)
- Núcleo: gpt-oss:20b (13.8GB ~92tok/s), qwen3:14b (9.3GB ~52tok/s), qwen2.5vl:7b (visión), bge-m3 (embeddings)
- Descartados: 32B densos (~6tok/s en 16GB VRAM), llama3.3:70b (42.5GB), GLM-Z1 local no existe
- Whisper: faster-whisper-medium en la Mac (faster-whisper sin ROCm en gfx1201); opcional whisper.cpp Vulkan distrobox
- Mac: proveedor nombrado "bazzite" http://192.168.100.209:11434/v1, context 32768 (OLLAMA_CONTEXT_LENGTH en contenedor)
- RAG bóveda: 322 notas, índice bge-m3 en la Mac vía red, SQLite + coseno (sin Chroma/Qdrant)
- Tiempo total día 1: 2-3 h sin opcionales
- Esperando: doctor enciende Bazzite + corre instalar_ia_local_bazzite.sh + avisa por Telegram

## Cierre con textura (14/09, 12:30)
- Texturizado COMPLETADO en la Bazzite esta mañana (sesión previa a este cron):
  TextureMesh sobre scene_dense.mvs + --mesh-file scene_dense_mesh.ply -> scene_dense_texture.ply (72.9 MB)
- Export/decimación: biblioteca_final.glb (42.5 MB) = malla 1,178,333 vértices /
  1,506,051 caras + textura JPEG 2048x2048 (873 KB, atlased), material PBR
  (baseColorTexture, roughness 1.0, metallic 0.0)
- GLB incrustado en biblioteca-virtual-v1.html vía GLB_ESCANEO_B64 (56.7 MB total);
  copia de respaldo idéntica en mecanografia_js/ (mismo SHA-256)
- Verificación por hash (12:24-12:30): GLB incrustado == biblioteca_final.glb
  (SHA-256 daab3cae...); sintaxis del módulo OK (node --check); body completo
- Textura validada: JPEG real (ffd8) 2048x2048, extraída del buffer del GLB
- Nota: las caras del GLB se declaran como índices (indices accessor), no como
  caras explícitas; el GLB es triangularizado y apto para three.js/PlayCanvas
- Prueba visual WebGL pendiente del doctor: el cron corre con el navegador de
  automatización sin WebGL; el entregable se valida con la prueba del botón
  "Ver escaneo real" en el Chrome del doctor
- La Bazzite no se encendió en esta pasada (trabajo ya realizado; no fue necesario)
