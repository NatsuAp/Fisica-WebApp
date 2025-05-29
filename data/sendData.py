import smtplib
import ssl
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import os

def enviar_pdf_por_correo(correo, estudiantes):
    load_dotenv()
    # Crear el mensaje
    remitente = os.getenv('CorreoRemitente')
    print(remitente)
    contraseña = os.getenv('contrasenaRemitente')
    print(contraseña)
    ruta_pdf = 'pdfs\Experimento_MRU.pdf'  # Ruta del archivo PDF que deseas enviar
    destinatario = correo
    asunto = 'Taller MRU'
    cuerpo = f'Taller movimiento rectilineo uniforme de: {estudiantes}'  
    mensaje = EmailMessage()
    mensaje['Subject'] = asunto
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje.set_content(cuerpo)
          
    # Adjuntar PDF
    with open(ruta_pdf, 'rb') as f:
        pdf_data = f.read()
        nombre_archivo = os.path.basename(ruta_pdf)
        mensaje.add_attachment(pdf_data, maintype='application', subtype='pdf', filename=nombre_archivo)

    # Configurar y enviar
    contexto = ssl.create_default_context()
    print("holaaaaaaaaaaaaaaa")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as servidor:
        servidor.login(remitente, contraseña)
        servidor.send_message(mensaje)
        print("Correo enviado con éxito.")
