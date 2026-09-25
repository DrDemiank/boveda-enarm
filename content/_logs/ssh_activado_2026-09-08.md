SSH ACTIVADO EN LA MAC — 08/09/2026
====================================
Metodo: osascript "with administrator privileges" (cuadro nativo de contrasena
en pantalla, tecleado por el usuario; la clave nunca paso por el agente).
Comando ejecutado: launchctl load -w /System/Library/LaunchDaemons/ssh.plist
Estado verificado:
- launchctl print-disabled system => "com.openssh.sshd" => false (habilitado)
- Puerto 22 ABIERTO (listener activo)
- Prueba externa: ssh a 192.168.100.24 responde con oferta (publickey,password)
- Permission denied en BatchMode = correcto: no hay llave autorizada todavia

PASO SIGUIENTE (en Bazzite):
  ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519
  ssh-copy-id cesarnazinkurigarcia@192.168.100.24
  ssh cesarnazinkurigarcia@192.168.100.24 "echo CONEXION_OK"
Despues de eso, jarvis.py/Claude puede ejecutar sin contrasena:
  ssh cesarnazinkurigarcia@192.168.100.24 \
    "/Users/cesarnazinkurigarcia/.hermes/hermes-agent/venv/bin/hermes --continue jarvis_voz -z \"<transcripcion>\""
