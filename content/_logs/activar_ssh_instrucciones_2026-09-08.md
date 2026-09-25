# Activar SSH en la Mac

ACTIVACION DE SSH EN LA MAC — requiere SU contrasena (no la puedo escribir yo)

Opcion A (2 clics, sin Terminal):
  1. Menu Apple > Ajustes del Sistema (o Preferencias en Monterey) > General > Compartir
  2. Activar "Inicio de sesion remota" (Remote Login)

Opcion B (Terminal de la Mac, pegue esto):
  sudo systemsetup -setremotelogin on
  (pedira SU contrasena de sesion)

Despues de eso, desde Bazzite pruebe:
  ssh cesarnazinkurigarcia@192.168.100.24 'echo CONEXION_OK'

Y para que Claude/jarvis.py no pidan clave nunca, en Bazzite:
  ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519
  ssh-copy-id cesarnazinkurigarcia@192.168.100.24