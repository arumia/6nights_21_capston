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
sudo apt install -y git python3.9
git clone https://github.com/arumia/6nights_21_capston
cd 6nights_21_capston
python -m venv venv
pip3 install -r requirments.txt

#pip 만들기
pip freeze > requirments.txt
```

### git 명령어
```
git add .
git config --global.user.email "내 이메일"
git config --global.user.name "내 닉네임"
git commit -m "커밋내용"
git push

git reset HEAD ... ...파일 지우기
```

### GPS 참고 문서
https://techlog.gurucat.net/239

### CSS는 bootstrap
공식문서: https://getbootstrap.com/docs/5.0/forms/layout/

### 카카오지도 API
공식문서: https://apis.map.kakao.com/web/guide/