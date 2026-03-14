# Proyecto Final – AP Physics

Aplicación web desarrollada como proyecto final para Materia de Ap physics en el colegio.  
Permite visualizar y analizar datos de un experimento realizado con una maqueta conectada a Arduino.

Nota: La aplicación todavía funciona, pero no es posible conectar nuevos datos porque depende de la maqueta física utilizada en clase.

## Cómo ejecutar el proyecto

1. Descargar la imagen de Docker

docker pull ghcr.io/natsuap/fisica-webapp:f806308

2. Ejecutar el contenedor

docker run -p 8501:8501 fisica_app

3. Abrir la aplicación

Una vez iniciado el contenedor, la terminal mostrará el enlace para acceder a la aplicación.

Abrir en el navegador:

http://localhost:8501

