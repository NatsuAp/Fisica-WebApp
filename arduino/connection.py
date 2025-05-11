import serial

arduino = None 
#Si esta conectado al arduino y recibio los datos correctamente
def checkConnection():
    try:
     #El primer parametro es el puerto
     #baudrate es la velocidad de transmision de datos en baudios pr segundo TODO:Verificar en el arudino el "Serial.begin(9600);", en este caso se usara 9600 por defecto
     #timeout es la cantidad de tiempo que esperara para leer datos antes de rendirse
        arduino = serial.Serial("COM3", baudrate=9600, timeout=1)
        
    except:
         print("Error de conexion con arduino")
         return False
    return True

def dataRetrieval():
    return str(arduino.readline())
