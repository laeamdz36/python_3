"""Modulo para enviar emails"""

from email.message import EmailMessage
import ssl
import smtplib

pws = "polqnpilozmwnrcw"
origin_email = "luis3mendez6@gmail.com"
target_email = "luis3mendez6@gmail.com"
contenido = """Hola Mundo Mundial"""


# Configuracion de envio
e_mail = EmailMessage()
e_mail["From"] = origin_email
e_mail["To"] = target_email
e_mail.set_content(contenido)

e_mail["Subject"] = "Nuevo Correo"

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as send_mail:
    send_mail.login(origin_email, pws)
    send_mail.sendmail(origin_email, target_email, e_mail.as_string())
