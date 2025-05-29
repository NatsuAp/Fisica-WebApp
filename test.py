import time
import serial.tools.list_ports

import threading

arduino = None
portName = None

#Si esta conectado al arduino y recibio los datos correctamente
def checkConnection(userPort = None):
    global portName 
    
    try:
     #El primer parametro es el puerto
     #baudrate es la velocidad de transmision de datos en baudios pr segundo TODO:Verificar en el arudino el "Serial.begin(9600);", en este caso se usara 9600 por defecto
     #timeout es la cantidad de tiempo que esperara para leer datos antes de rendirse
     if userPort is None:
        
        ports = list(serial.tools.list_ports.comports())
        print(ports)
        for port in ports:
          print(port)
          if "usb"  in port.description.lower() or "arduino" in port.description.lower():
                print(port.name)
                arduino = serial.Serial(port.device, baudrate=9600, timeout=5)
                print("puerto" + port.device)
                portName= port.device
                print(arduino)
                return arduino
          
     if userPort is not None:
       arduino = serial.Serial(userPort, baudrate=9600, timeout=5)
       portName = userPort
       print("aaa")
       return arduino   
        
    except Exception as e:
         print(e)
         print("Error de conexion con arduino")
         if userPort is None:
          return None
         else:
          return "userError"
         

if __name__ == "__main__":
   
   connection = checkConnection()
   while True:
    print(connection.read_all().decode())
    time.sleep(1)



   
