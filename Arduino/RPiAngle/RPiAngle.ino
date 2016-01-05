#include <Servo.h>
Servo angleServo;
int anglePin = 9;
int angle = 90;
float RU;

void setup() {
  Serial.begin(9600);
  angleServo.attach(anglePin);
}

void loop() {
  if(Serial.available() >0){
    RU = Serial.parseFloat();
  }else{
    RU = 0.0;
  }
  angle = 90 + (RU * 20);
  angleServo.write(angle);
  delay(30);
  Serial.println(RU,angle);
}
