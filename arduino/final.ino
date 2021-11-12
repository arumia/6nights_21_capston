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
#define SWITCH1 2
#define SWITCH2 3

int Push_speed=0; // 엑츄에이터 밀기 속도 설정 0~255
int Oger_speed=0; // 오거 속도 설정 0~255
int flag = 0;

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
	digitalWrite(ENA,HIGH);
	// 스위치 핀설정
	pinMode(SWITCH1, INPUT);
	pinMode(SWITCH2, INPUT);
	// 오거 핀설정
	pinMode(PWM,OUTPUT);
	pinMode(Oger_DIR,OUTPUT);
  
	attachInterrupt(digitalPinToInterrupt(SWITCH2), SWITCH, CHANGE);
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
			
			digitalWrite(Oger_DIR, LOW); // 시계방향 회전 시작
			for(Oger_speed=0; Oger_speed<11; Oger_speed++){
				if(flag == 0){
					delay(10);
					analogWrite(PWM, Oger_speed);
				}
			}
			
			// 위로 올리기
			for (int i=0; i<30000; i++)    //Forward 5000 steps
			{
				//Serial.println(flag);
				digitalWrite(DIR,LOW);
				//digitalWrite(ENA,HIGH);
				digitalWrite(PUL,HIGH);
				delayMicroseconds(50);
				digitalWrite(PUL,LOW);
				delayMicroseconds(50);
			}
			
			StopAndPush()
		}
		
		else if(input == 'd') //시리얼로 d 입력을 받았을 때 아레로 작동
		{
			Serial.print("echo: ");
			Serial.println("밑으로 내려가는 중...");
			
			digitalWrite(Oger_DIR, HIGH); // 반시계방향 회전 시작
			for(Oger_speed=0; Oger_speed<255; Oger_speed++){
				if(flag == 0){
					delay(10);
					analogWrite(PWM, Oger_speed);
				}
			}

			// 아래로 내리기
			flag = 0;
			for (int i=0; i<30000; i++)   //Backward 5000 steps
			{
				digitalWrite(DIR,HIGH);
				//digitalWrite(ENA,HIGH);
				digitalWrite(PUL,HIGH);
				delayMicroseconds(50);
				digitalWrite(PUL,LOW);
				delayMicroseconds(50);
			}

			//delay(10000);       // 3초동안 역방향 회전
			for(Oger_speed; Oger_speed>=0; Oger_speed--){
				delay(10);
				analogWrite(PWM, Oger_speed);
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

void init(){
}

void StopAndPush(){
	digitalWrite(EN3, HIGH); // 모터B설정
	digitalWrite(EN4, LOW);
	for(Motor_speed=0; Motor_speed<256; Motor_speed++){
	  analogWrite(ENB, Motor_speed);
	}
	
	for(Motor_speed=255; Motor_speed>0; Motor_speed--){
	  analogWrite(ENB, Motor_speed);
	}
	
	// 모터A,B 역방향
	digitalWrite(EN3, LOW); // 모터B설정
	digitalWrite(EN4, HIGH);
	for(Motor_speed=0; Motor_speed<256; Motor_speed++){
		analogWrite(ENB, Motor_speed);
	}
	
	for(Motor_speed=255; Motor_speed>0; Motor_speed--){
		analogWrite(ENB, Motor_speed);
	}
}