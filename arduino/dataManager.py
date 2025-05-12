def dataRetrieval(arduino):
    data = str(arduino.readline().decode(errors='ignore'))
    print(data)
    
   
    #dataArr.insert(data)
    return 