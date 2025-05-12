import io
import serial
import serial.tools.list_ports

arduino = None

#Si esta conectado al arduino y recibio los datos correctamente
def checkConnection():
    try:
     #El primer parametro es el puerto
     #baudrate es la velocidad de transmision de datos en baudios pr segundo TODO:Verificar en el arudino el "Serial.begin(9600);", en este caso se usara 9600 por defecto
     #timeout es la cantidad de tiempo que esperara para leer datos antes de rendirse
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
          if "USB"  in port.description:
                print(port.name)
                arduino = serial.Serial(port.name, baudrate=9600, timeout=5)
                return arduino
        
    except Exception as e:
         print(e)
         print("Error de conexion con arduino")
         return None

dataArr = []
def dataRetrieval(arduino):
    data = str(arduino.readline())
    print(data)
    
   
    #dataArr.insert(data)
    return "hola"