FROM python:3.9

COPY requirements.txt ./

RUN apt update && apt upgrade -y
RUN apt install python3-dev gcc build-essential -y
ENV CFLAGS="-fcommon"
RUN pip install -r requirements.txt

COPY manage.py gunicorn-cfg.py django_start.sh ./
COPY app app
COPY authentication authentication
COPY core core
COPY staticfiles staticfiles
COPY media media

RUN python manage.py makemigrations app
RUN python manage.py migrate

EXPOSE 8000
CMD ["bash", "django_start.sh"]
