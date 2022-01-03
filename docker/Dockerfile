FROM python:3.6

COPY manage.py gunicorn-cfg.py requirements.txt ./
COPY app app
COPY authentication authentication
COPY core core
COPY staticfiles staticfiles
COPY media media

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD ["bash", "django_start.sh"]
