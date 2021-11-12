// 아두이노 연결된 핀 설정
#define PWM 10
#define DIR 9
#define SWITCH1 2
int Motor_speed=0; // 모터 속도 PWM 100으로 설정 0~255
int flag = 0;

void setup() {
  pinMode(SWITCH1, INPUT);
  pinMode(PWM,OUTPUT);
  pinMode(DIR,OUTPUT);
  Serial.begin(115200); //시리얼 포트를 115200bps속도로 시작

  attachInterrupt(digitalPinToInterrupt(SWITCH1), SWITCH, CHANGE);
}

void loop() {
	if(Serial.available())
	{
		char input = Serial.read();
		
		if(input == 'u') // 시리얼로 u 입력을 받았을 떄 위로 작동
		{
  // if(digitalRead(SWITCH1) == HIGH){
  //   Serial.println("SWITCH1");
  // }
      flag = 0;
      digitalWrite(DIR, LOW); // 시계방향
      for(Motor_speed=0; Motor_speed<255; Motor_speed++){
        if(flag == 0){
          delay(10);
          analogWrite(PWM, Motor_speed);
        }
      }
      delay(5000);
      for(Motor_speed; Motor_speed>0; Motor_speed--){
        delay(10);
        analogWrite(PWM, Motor_speed);
      }
//      delay(5000);
    }
    else if(input == 'd') //시리얼로 d 입력을 받았을 때 아레로 작동
		{
      digitalWrite(DIR, HIGH); //반시계방향
      for(Motor_speed=0; Motor_speed<255; Motor_speed++){
        delay(10);
        analogWrite(PWM, Motor_speed);
      }
      delay(5000);
      for(Motor_speed; Motor_speed>0; Motor_speed--){
        delay(10);
        analogWrite(PWM, Motor_speed);
      }
//      delay(5000);
    }
  }
}
void SWITCH(){
 if(digitalRead(SWITCH1) == LOW){
   Serial.println("interrupt!!!!Switch on!");
   Serial.println(flag);
   flag = 1;
   if(Motor_speed>0){
     for(Motor_speed; Motor_speed>0; Motor_speed--){
       for(int i=0; i<10; i++)
         delayMicroseconds(1000);
       analogWrite(PWM, Motor_speed);
     }
   }
 }
 else{
//   flag = 0;
//   Serial.println("Switch off");
   }
}
