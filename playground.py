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

def tester():
	return "<"+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+">"+"/n"
    
arduino = finduino()


o = "<09990>\n"
i = "<90009>\n"

t = "<90990>\n"

print(t.encode())
arduino.write(t.encode())
time.sleep(1)

print ("Done.")
arduino.close()
print( "Closed port.")