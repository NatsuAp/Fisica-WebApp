@echo off
setlocal

:: Ruta al entorno virtual (ajusta si es diferente)
set VENV_DIR=.venv
set APP_FILE=app.py



:: Verificar que el archivo de la app exista
if not exist %APP_FILE% (
    echo No se encontró el archivo %APP_FILE%.
    exit /b 1
)

:: Ejecutar la app de Streamlit
echo Ejecutando Streamlit...
docker run -p 8501:8501 fisica_app

endlocal
