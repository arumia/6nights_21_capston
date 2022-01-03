FROM python:3.9

COPY manage.py gunicorn-cfg.py requirements.txt ./
COPY app app
COPY authentication authentication
COPY core core
COPY staticfiles staticfiles
COPY media media

RUN apt update && apt upgrade -y
RUN apt install python3-dev gcc build-essential -y
ENV CFLAGS="-fcommon"
RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD ["bash", "django_start.sh"]
