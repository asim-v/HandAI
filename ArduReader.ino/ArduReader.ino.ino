#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver servos = Adafruit_PWMServoDriver(0x40);

unsigned int pos0=172; // ancho de pulso en cuentas para pocicion 0°
unsigned int pos180=565; // ancho de pulso en cuentas para la pocicion 180°

void setup() {
  servos.begin();  
  servos.setPWMFreq(60); //Frecuecia PWM de 60Hz o T=16,66ms
  Serial.begin(9600);
}
void loop() {

  while(!Serial.available()); // wait till data to be filled in serial buffer

  String incommingStr = Serial.readStringUntil('\n'); // read the complete string
  move_servos(incommingStr);
}

void move_servos(String s){

  //Están volteados por que algunos servos están volteados.
  int out1 = map(s.substring(0,2).toInt(),99,0,172,565);  
  int out2 = map(s.substring(2,4).toInt(),99,0,172,565);  
  int out3 = map(s.substring(4,6).toInt(),0,99,172,565);  
  int out4 = map(s.substring(6,8).toInt(),99,0,172,565);  
  int out5 = map(s.substring(8,10).toInt(),0,99,172,565);  
  int out6 = map(s.substring(10,12).toInt(),0,99,172,565);  
  servos.setPWM(0,0,out4);
  servos.setPWM(1,0,out3);
  servos.setPWM(2,0,out2);
  servos.setPWM(3,0,out1);
  servos.setPWM(4,0,out5);  
  servos.setPWM(5,0,out6);  
}
