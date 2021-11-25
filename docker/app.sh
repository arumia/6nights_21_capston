#!/usr/bin/env bash

python3 /root/app/tornado/server.py&
python3 /root/app/template/manage.py runserver sami.works:8000&
