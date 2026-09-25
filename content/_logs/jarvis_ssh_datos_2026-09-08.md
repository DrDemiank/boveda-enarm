DATOS VERIFICADOS EN VIVO (08/09/2026, Mac del Dr. Demian):

1. RUTA DEL BINARIO HERMES:
   /Users/cesarnazinkurigarcia/.hermes/hermes-agent/venv/bin/hermes
   (version v0.21.0, instalacion git)

2. MODO ONE-SHOT CONFIRMADO FUNCIONAL:
   hermes -z "prompt"                          -> respuesta y sale (18 s medidos)
   hermes --continue jarvis_voz -z "prompt"    -> sesion continua con memoria (27-39 s)
   La sesion "jarvis_voz" ya existe y conserva contexto entre llamadas (verificado
   con palabra de prueba jarvis-123, recordada y luego borrada).

3. SSH (Remote Login) EN ESTA MAC: DESACTIVADO
   /System/Library/LaunchDaemons/ssh.plist tiene Disabled = 1 y el puerto 22 esta
   cerrado. Para que Bazzite entre por SSH hay que activarlo:
     Preferencias del Sistema > Compartir > Inicio de sesion remota (Remote Login)
   (o con admin: sudo systemsetup -setremotelogin on)
   IP local de la Mac: 192.168.100.24
   Usuario SSH: cesarnazinkurigarcia

4. LLAVE SSH: conviene generar en Bazzite (ssh-keygen) y autorizarla en la Mac
   (~/.ssh/authorized_keys) para que jarvis.py no pida contrasena nunca.