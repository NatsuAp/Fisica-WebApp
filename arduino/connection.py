import time
import serial.tools.list_ports

import threading
from Utils import pageManager
arduino = None
portName = None
#Si esta conectado al arduino y recibio los datos correctamente
def checkConnection(userPort):
    global portName 
    
    try:
     #El primer parametro es el puerto
     #baudrate es la velocidad de transmision de datos en baudios pr segundo TODO:Verificar en el arudino el "Serial.begin(9600);", en este caso se usara 9600 por defecto
     #timeout es la cantidad de tiempo que esperara para leer datos antes de rendirse
     if userPort is None:
        
        ports = list(serial.tools.list_ports.comports())
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

dataArr = []
# TODO: Terminar esta funcion
def checkConstantConnection(port):
  print("entro a la funcion")
  time.sleep(5)
  while True:
    myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
    if port not in myports:
      print ("Se desconecto el arduino")
      pageManager.page = "error"
      break
    time.sleep(1)   
    
   
          
def asyncCall():
  global portName
  try:
    port_controller = threading.Thread(target=checkConstantConnection, args=(portName,))
    port_controller.setDaemon(True)
    port_controller.start()
    print("empezo el nuevo thread")
  except Exception as e:
    print("Error al iniciar el hilo", e)
    return False
  print("Si va a retornar true")
  return True
  