/*
L298N, TB6600, MD30C 모터드라이버
*/
// L298N 핀 설정(액츄에이터 밀기부)
#define ENB 10 //L298N PWM핀
#define EN3 9 //HIGH=정방향
#define EN4 8 //HIGH=역방향
// TB6600 핀 설정(위 아래)
#define PUL 7 //define Pulse pin
#define DIR 6 //define Direction pin
#define ENA 5 //define Enable Pin
// MD30C (오거 회전부)
#define PWM 11
#define Oger_DIR 12
// 스위치
#define SWITCH_UP 2
#define SWITCH_OGER 3

int Push_speed=0; // 엑츄에이터 밀기 속도 설정 0~255
int Oger_speed=0; // 오거 속도 설정 0~255
int flag = 0;
int flag_up = 0;

void setup()
{
  Serial.begin(115200);
  // 밀기 엑추에이터 PWM 제어핀 출력 설정
  pinMode(ENB,OUTPUT);
  // 밀기 엑추에이터 방향 제어핀 출력 설정
  pinMode(EN3,OUTPUT);
  pinMode(EN4,OUTPUT);
  // TB6600 핀설정
  pinMode (PUL, OUTPUT);
  pinMode (DIR, OUTPUT);
  pinMode (ENA, OUTPUT);
  digitalWrite(DIR,LOW);
  digitalWrite(ENA,HIGH);
  // 스위치 핀설정
  pinMode(SWITCH_UP, INPUT);
  pinMode(SWITCH_OGER, INPUT);
  // 오거 핀설정
  pinMode(PWM,OUTPUT);
  pinMode(Oger_DIR,OUTPUT);

//   attachInterrupt(digitalPinToInterrupt(SWITCH_UP), switchup, CHANGE);
//   attachInterrupt(digitalPinToInterrupt(SWITCH_OGER), switchoger, CHANGE);

}

void loop()
{
  if(Serial.available())
  {
    char input = Serial.read();

    if(input == 'u') // 시리얼로 u 입력을 받았을 떄 위로 작동
    {
      Serial.print("echo: ");
      Serial.println("위로 올라가는 중...");

      digitalWrite(Oger_DIR, HIGH); // 시계방향 회전 시작
      for(Oger_speed=0; Oger_speed<51; Oger_speed++){
        if(flag == 0){
          delay(10);
          analogWrite(PWM, Oger_speed);
        }
      }
      digitalWrite(DIR,LOW);
      digitalWrite(ENA,HIGH);
      // 위로 올리기
      while(1){
        if(digitalRead(SWITCH_UP) == LOW){
                Serial.println("upper switch up!");
                return;
        }
        digitalWrite(PUL,HIGH);
        delayMicroseconds(50);
        digitalWrite(PUL,LOW);
        delayMicroseconds(50);
      }

      while(1){
        if(digitalRead(SWITCH_UP) == LOW){
            if(digitalRead(SWITCH_OGER) == LOW){
                Serial.println("Oger switch up!");
                analogWrite(PWM, 0);
                break;
            }
        }
      }
//      StopAndPush();
    }

    else if(input == 'd') //시리얼로 d 입력을 받았을 때 아레로 작동
    {
      Serial.print("echo: ");
      Serial.println("초기화중...");
      InitPosition();
      Serial.print("echo: ");
      Serial.println("밑으로 내려가는 중...");

      digitalWrite(Oger_DIR, LOW); // 반시계방향 회전 시작
      for(Oger_speed=0; Oger_speed<255; Oger_speed++){
        if(flag == 0){
          delay(10);
          analogWrite(PWM, Oger_speed);
        }
      }

      // 아래로 내리기
      digitalWrite(DIR,HIGH);
      digitalWrite(ENA,HIGH);
      flag = 0;
      for (int i=0; i<50; i++)   //310이 최고 적절값
      {
        for (int j=0; j<1000; j++){
          digitalWrite(PUL,HIGH);
          delayMicroseconds(25);
          digitalWrite(PUL,LOW);
          delayMicroseconds(25);
        }
      }

      delay(1500);       // 3초동안 역방향 회전
      for(Oger_speed; Oger_speed>=0; Oger_speed--){
        delay(10);
        analogWrite(PWM, Oger_speed);
      }
    }
  }
}

void switchup(){
  if(digitalRead(SWITCH_UP) == LOW){
    flag_up = 1;
    Serial.println("Switch_UP is on!");
  }
}
void switchoger(){
  if(digitalRead(SWITCH_UP) == LOW){
    if(digitalRead(SWITCH_OGER) == LOW){
      Serial.println("interrupt!!!!Switch on!");
      flag = 1;
      Serial.println(flag);
      analogWrite(PWM, 0);
      // if(Motor_speed>0){
      //  for(Motor_speed; Motor_speed>=0; Motor_speed--){
      //    for(int i=0; i<10; i++)
      //      delayMicroseconds(1000);
      //    analogWrite(PWM, Motor_speed);
      //  }
      // }
    }
  }
}

void InitPosition(){
  digitalWrite(DIR,HIGH);
  digitalWrite(ENA,HIGH);
  for (int j=0; j<5000; j++){
    digitalWrite(PUL,HIGH);
    delayMicroseconds(50);
    digitalWrite(PUL,LOW);
    delayMicroseconds(50);
  }
  flag_up = 0;
  digitalWrite(DIR,LOW);
  digitalWrite(ENA,HIGH);
  while(1){
    digitalWrite(PUL,HIGH);
    delayMicroseconds(50);
    digitalWrite(PUL,LOW);
    delayMicroseconds(50);
    if(digitalRead(SWITCH_UP) == LOW){
        Serial.println("init switch up!");
        return;
    }
  }
}

void StopAndPush(){
  digitalWrite(EN3, HIGH); // 모터B설정
  digitalWrite(EN4, LOW);
  for(Push_speed=0; Push_speed<255; Push_speed++){
    analogWrite(ENB, Push_speed);
  }
  delay(19000);          // 3초동안 정방향 회전
  for(Push_speed; Push_speed>0; Push_speed--){
    analogWrite(ENB, Push_speed);
  }

  // 모터A,B 역방향
  digitalWrite(EN3, LOW); // 모터B설정
  digitalWrite(EN4, HIGH);
  for(Push_speed=0; Push_speed<256; Push_speed++){
    analogWrite(ENB, Push_speed);
  }
  delay(19000);
  for(Push_speed=255; Push_speed>0; Push_speed--){
    analogWrite(ENB, Push_speed);
  }
}