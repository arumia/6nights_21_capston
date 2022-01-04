#!/bin/bash
# Apache License 2.0
# Copyright (c) 2020, ROBOTIS CO., LTD.

echo ""
echo "장고 서버 실행 스크립트"
echo "[Note] 0.1ver"
echo ""
echo "PRESS [ENTER] TO CONTINUE THE INSTALLATION"
echo "IF YOU WANT TO CANCEL, PRESS [CTRL] + [C]"
read

echo "[Set the target ROS version and name of colcon workspace]"
source venv/bin/activate

echo "[Set Djnago]"
python3 manage.py makemigrations app
python3 manage.py migrate

echo "[Start Djnago]"
python3 manage.py runserver sami.works:8000 &

echo "[Start Selery]"
celery -A core worker -l info -B &

echo "[Start Tornado]"
python3 ../tornado/server.py &

echo "[Complete!!!]"
while true; do
  sleep 5d # Waits 5 days.
done
