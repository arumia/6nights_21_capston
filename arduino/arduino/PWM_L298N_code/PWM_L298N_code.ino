/*
L298N 모터드라이버
http://www.devicemart.co.kr/
*/
// 아두이노 연결된 핀 설정
#define ENA 1
#define ENB 10
#define EN1 2
#define EN2 3
#define EN3 9
#define EN4 8
int Motor_speed=255; // 모터 속도 PWM 100으로 설정 0~255
void setup()
{
Serial.begin(9600);
// PWM 제어핀 출력 설정
pinMode(ENA,OUTPUT);
pinMode(ENB,OUTPUT);
// 방향 제어핀 출력 설정
pinMode(EN1,OUTPUT);
pinMode(EN2,OUTPUT);
pinMode(EN3,OUTPUT);
pinMode(EN4,OUTPUT);
}
void loop()
{
	if(Serial.available())
	{
		char input = Serial.read();
		
		if(input == 'u') // 시리얼로 u 입력을 받았을 떄 위로 작동
		{
			// 모터 A,B 정방향
			//digitalWrite(EN1, HIGH);   // 모터A 설정 
			//digitalWrite(EN2, LOW);  
			//analogWrite(ENA, Motor_speed);  
			//digitalWrite(EN3, HIGH);  // 모터B설정
			//digitalWrite(EN4, LOW);
			for(Motor_speed=0; Motor_speed<256; Motor_speed++){
			  analogWrite(ENB, Motor_speed);
			}
			delay(3000);          // 3초동안 정방향 회전
			for(Motor_speed=255; Motor_speed>0; Motor_speed--){
			  analogWrite(ENB, Motor_speed);
			}
		}
		else if(input == 'd') //시리얼로 d 입력을 받았을 때 아레로 작동
		{
			// 모터A,B 역방향
			//digitalWrite(EN1, LOW);  // 모터A설정
			//digitalWrite(EN2, HIGH);  
			//analogWrite(ENA, Motor_speed);  
			digitalWrite(EN3, LOW); // 모터B설정
			digitalWrite(EN4, HIGH);
			for(Motor_speed=0; Motor_speed<256; Motor_speed++){
			  analogWrite(ENB, Motor_speed);
			}
			delay(10000);       // 3초동안 역방향 회전
			for(Motor_speed=255; Motor_speed>0; Motor_speed--){
			  analogWrite(ENB, Motor_speed);
			}
		}
	}
