LA PRUEBA SIGUE FALLANDO (puerto 22 rechaza). Diagnosticado con precision:

- El binario sshd existe (/usr/sbin/sshd) y su configuracion (/etc/ssh/sshd_config, 2024) OK
- El servicio com.openssh.sshd NO ESTA CARGADO en launchd ("Could not find service")
- El estado del sistema confirma: Remote Login sigue DESACTIVADO

Es decir: la casilla correcta sigue apagada. En Monterey en espanol, en
Preferencias del Sistema > Compartir, hay VARIAS casillas parecidas y es facil
confundirlas. La correcta es EXACTAMENTE:

  [x] Inicio de sesion remota      <- esta es (Remote Login)
  [ ] Compartir pantalla
  [ ] Acceso a mi Mac (Remote Apple Events)
  [ ] Compartir archivos

Al marcarla, debajo dira: "Inicio de sesion remota: Sesion remota activada." y a la
derecha mostrara la direccion 192.168.100.24. Si pide confirmacion, es la contrasena
de SU usuario (es admin).

ALTERNATIVA TERMINAL (la mas directa, en Terminal de la Mac):
  sudo systemsetup -setremotelogin on
  (pide contrasena; luego confirma con "y" si pregunta)

Y para verificar usted mismo sin volver a mi:
  ssh localhost -p 22
  (si pide contraseña o conecta: YA ESTA; si dice "Connection refused": sigue apagado)

Cuando el foco verde este EN VERDAD encendido, digame "listo" y repito la prueba.