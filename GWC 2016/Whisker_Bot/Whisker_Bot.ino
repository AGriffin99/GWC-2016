void setup() {
  // put your setup code here, to run once:
pinMode(5, INPUT);
pinMode(7, INPUT);
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
Serial.println(digitalRead(5));
Serial.println(digitalRead(7));
}
