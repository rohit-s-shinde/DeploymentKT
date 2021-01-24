FROM python:3.6

COPY /temp /temp

WORKDIR /temp

RUN pip install -U -r requirements.txt

EXPOSE 8000

RUN python manage.py migrate

CMD uwsgi --ini config.ini
