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

добавлена новая ветка 