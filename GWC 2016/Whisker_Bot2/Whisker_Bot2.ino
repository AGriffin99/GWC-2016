 #include <Servo.h>
 Servo servoRight;
 Servo servoLeft;
void setup() {
  // put your setup code here, to run once:
 servoLeft.attach(13);
 servoRight.attach(12);
pinMode(6, INPUT);
pinMode(8, INPUT);
Serial.begin(9600);
}
void backward(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  delay(500);
}

void forward(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
  delay(900);
}

void right(){
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1700);
}

void left(){
  servoLeft.writeMicroseconds(1500);
  
  servoRight.writeMicroseconds(1700);
}
void loop(){
  // put your main code here, to run repeatedly:
Serial.println(digitalRead(6));
//Serial.println(digitalRead(8));
if ((digitalRead(6)==0 ) &&(digitalRead(8)==0 )){
backward();
left();
}
if (digitalRead(6)==0){
  backward();
  right();
}
else if(digitalRead(8)==0){
  backward();
  left();
  
}
else{
  forward();
}

}


