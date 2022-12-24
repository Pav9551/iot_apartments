FROM python:3.8
WORKDIR /iot
COPY requirements.txt /iot
COPY . /iot
RUN pip3 install --upgrade pip -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

