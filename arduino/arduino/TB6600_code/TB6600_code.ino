#define SWITCH1 3
#define SWITCH2 2

int PUL=7; //define Pulse pin
int DIR=6; //define Direction pin
int ENA=5; //define Enable Pin
int flag = 0;

void setup() {
  pinMode (PUL, OUTPUT);
  pinMode (DIR, OUTPUT);
  pinMode (ENA, OUTPUT);
  pinMode(SWITCH1, INPUT);
  pinMode(SWITCH2, INPUT);
  
  Serial.begin(9600); //시리얼 포트를 9600bps로 시작
  attachInterrupt(digitalPinToInterrupt(SWITCH2), SWITCH, CHANGE);
}

void loop() {
  if(Serial.available())
	{
		char input = Serial.read();
		
		if(input == 'u') // 시리얼로 u 입력을 받았을 떄 위로 작동
		{
      Serial.print("echo: ");
      Serial.println("위로 올라가는 중...");
      flag = 0;
      for (int i=0; i<30000; i++)    //Forward 5000 steps
      {
          //Serial.println(flag);
          digitalWrite(DIR,LOW);
          digitalWrite(ENA,HIGH);
          digitalWrite(PUL,HIGH);
          delayMicroseconds(50);
          digitalWrite(PUL,LOW);
          delayMicroseconds(50);
      }
    }
    else if(input == 'd') //시리얼로 d 입력을 받았을 때 아레로 작동
    {
      Serial.print("echo: ");
      Serial.println("밑으로 내려가는 중...");
      flag = 0;
      for (int i=0; i<30000; i++)   //Backward 5000 steps
      {
        digitalWrite(DIR,HIGH);
        digitalWrite(ENA,HIGH);
        digitalWrite(PUL,HIGH);
        delayMicroseconds(50);
        digitalWrite(PUL,LOW);
        delayMicroseconds(50);
      }
    }
  }
}

void SWITCH(){
// if(digitalRead(SWITCH1) == LOW){
   Serial.println("interrupt!!!!Switch on!");
   Serial.println(flag);
   flag = 1;
//   if(Motor_speed>0){
//     for(Motor_speed; Motor_speed>0; Motor_speed--){
//       for(int i=0; i<10; i++)
//         delayMicroseconds(1000);
//       analogWrite(PWM, Motor_speed);
//     }
//   }
// }
// else{
//   flag = 0;
   // Serial.println("Switch off");
//   }
}
