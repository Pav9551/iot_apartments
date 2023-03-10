# iot_apartments
### Дипломная работа по курсу python-разработчик по теме "Умная гостиница"
Web-сервис на Django визуализирует данные датчиков о состоянии окружающей среды в апартамантах.
Данный сервис является составной частью системы IOT.
#### Диаграмма прецидентов системы представлена на рисунке
![Alt-текст](https://github.com/Pav9551/iot_apartments/blob/main/use%20case.jpg "use case")
#### Установка

 - Для установки веб-сервиса необходимо скопировать содержимое репозитория на диск:
```curl   
git clone https://github.com/Pav9551/iot_apartments
```
 - перейти в папку iot с файлом manage.py:
```curl 
cd iot
 ```
 - Для работы сервиса необходимо поставить зависимости
```curl   
pip3 install -r requirements.txt
```

 - в iot_apartments создать файл .env c ключом:
```curl 
SECRET_KEY = 'django-insecure-1234567890'
 ```

 - сбросить все миграции:
```curl 
python manage.py migrate iotapp zero --fake
```
 - удалить файлы миграции в каталоге migrations:
```curl 
0001_initial.py и др. 000...
```
 - создать файлы миграции командой:
```curl 
python manage.py makemigrations
```
 - сделать миграции в базу командой:
```curl 
python manage.py migrate
```
 - создать суперпользователя:
```curl 
python manage.py createsuperuser
```
## Пример использования
Чтобы протестировать веб-сервис необходимо:
 - загрузить данные в базу:
```curl 
python manage.py fill_states
```
 - запустить сервер:
```curl 
python manage.py runserver
```
 - перейти по адресу и посмотреть данные Datas через админку:
```curl 
http://127.0.0.1:8000/admin/
```
если порт забился:
```curl 
sudo fuser -k 8000/tcp
```
