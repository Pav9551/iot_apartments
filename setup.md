sudo apt-get update обновить индекс пакетов систем Ubuntu и Debian 

sudo apt -y install mc установка mc

cd home

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru

1 s

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04

1 s

mqtt_user


1

git clone https://github.com/Pav9551/iot_apartments

sudo chmod 777 ./mosquitto/config/passwd

docker exec -it mosquitto mosquitto_passwd -c  /mosquitto/config/passwd

touch ./mosquitto/log/mosquitto.log
sudo chmod 777 ./mosquitto/log/mosquitto.log

touch ./mosquitto/data/mosquitto.db.new
sudo chmod 777 -R ./mosquitto

docker-compose exec mosquitto mosquitto_passwd -c /mosquitto/config/passwd mqtt_user

ввести пароль для первого пользователя

docker-compose exec mosquitto mosquitto_passwd -b /mosquitto/config/passwd seconduser shoaCh3ohnokeathal6eeH2marei2o


docker-compose run mqtttodb  pip3 install django-chartjs

git шпаргалка 
https://agladky.ru/blog/git-cheat-sheet/
git config --list
работа с ветками
https://sysout.ru/rabota-s-vetkami-v-git/?ysclid=ldljbgmq21102141308

Перед миграцией выключить 
docker-compose stop mqtttodb

После миграциеи включить 
docker-compose start mqtttodb

https://sysout.ru/rabota-s-vetkami-v-git/?ysclid=ldljbgmq21102141308
docker-compose run  mqtttodb python manage.py makemigrations

docker-compose run  mqtttodb python manage.py migrate

docker-compose run  mqtttodb python manage.py fill_states

как настраивать postgre

https://habr.com/ru/post/578744/


