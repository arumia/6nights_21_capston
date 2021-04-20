# 6nights_21_capston

## 소개
2021년 캡스톤 디자인 프로젝트(자동토양시료채취포장기 제어부)

## 소프트웨어 모델링
|byte|형식|설명|
|:---:|:---:|:---:|
|4byte|(int)|과수 ID|
|2byte | 0x0000 | 작물(목적 식물) 년식 
|4byte|(Float)|GPS 위도|
|4byte|(Float)|GPS 경도|
|4byte|(Float)|GPS 높이(해발고도)|


### 개발 환경
PyCharm 2021.1

Python 3.9.4

### 실행 환경
HW: 라즈베리파이 4B 4gb

OS: Raspberry Pi OS Lite

### 파이썬 설정
```
sudo apt update && sudo apt upgrade -y
sudo apt install -y git
git clone https://github.com/arumia/6nights_21_capston
cd 6nights_21_capston
pip3 install -r requirments.txt
```