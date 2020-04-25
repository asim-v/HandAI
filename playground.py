import serial, time
import string
import random

def finduino():
  print('Searching arduino...\n')  
  for i in range(16):
    try:
      arduino = serial.Serial('COM'+str(i), 9600)
      print("Arduino found at: " + 'COM'+str(i))
      time.sleep(2)
      return arduino
      break
    except :pass


    
arduino = finduino()

o = "<90990>\n"
i = "<09009>\n"

abierto= "000000000000>\n"
cerrado = "999999999999>\n"

arduino.write(abierto.encode())
time.sleep(1)

print ("Done.")
arduino.close()
print( "Closed port.")