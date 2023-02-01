from django.core.management.base import BaseCommand
from pathlib import Path
import paho.mqtt.client as mqtt_client
from iotapp.models import Building, Room, DeviceType, Plan, Device, Data
from os import environ
import sys
from django.utils import timezone
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
goods_path = (BASE_DIR / 'goods.xlsx').__str__()

broker = environ.get("MQTT_HOST", "localhost")
port = 1883
topic = "cab2/sensor/cab2_sound/state"

topic_sub = "cab1/sensor/cab1_sound/state"
topic_sub = [("cab1/sensor/#", 0),
            ("room1/sensor/#", 0),
            ("room2/sensor/#", 0),
            ("room3/sensor/#", 0),
            ("room4/sensor/#", 0),
            ("room5/sensor/#", 0),
            ("room6/sensor/#", 0),
            ("room7/sensor/#", 0),
            ("room8/sensor/#", 0),
            ("room9/sensor/#", 0),
            ("room10/sensor/#", 0),
            ("corridor1/sensor/#", 0),
            ("corridor2/sensor/#", 0),
             ]
# generate client ID with pub prefix randomly
client_id = '123'
username = 'mqtt_user'
password = 'mqtt_user'
deviceId = "1"
listofdata = []
count = 0
count_del = 0
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc==0:
            print("Successfully connected to MQTT broker")
        else:
            print("Failed to connect, return code %d", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
def publish(client, status):
    msg = "{\"action\":\"command/insert\",\"deviceId\":\""+deviceId+"\",\"command\":{\"command\":\"LED_control\",\"parameters\":{\"led\":\""+status+"\"}}}"
    msg = status
    result = client.publish(msg,topic)
    msg_status = result[0]
    if msg_status ==0:
        print(f"message : {msg} sent to topic {topic}")

    else:
        print(f"Failed to send message to topic {topic}")
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        #print(f"Recieved '{msg.payload.decode()}' from '{msg.topic}' topic")
        #print(msg.topic.split("/")[0])
        devices = Device.objects.filter(mqttPath = msg.topic)
        global count# костыль
        global listofdata  # костыль
        global count_del # костыль
        if len(devices) > 0:
            device = devices[0]
        else:
            #создание нового устройства
            print("обнаружено новое устройство")
            building, created = Building.objects.get_or_create(name="Yakor", address ="Москва, Потаповский переулок ст1", disabled = True)
            room, created = Room.objects.get_or_create(name = msg.topic.split("/")[0], mqttPath = msg.topic.split("/")[0],  disabled=True, building = building)
            deviceType, created  = DeviceType.objects.get_or_create(name = "ESP32")
            plan, created = Plan.objects.get_or_create(name="1 этаж", building = building)
            device, created = Device.objects.get_or_create(name = msg.topic.split("/")[2], mqttPath = msg.topic,  positionX=0, positionY=0,
            enabled = True, type = deviceType, room = room, plan = plan)
        new_data = Data(name = msg.topic.split("/")[2], value = float(msg.payload.decode()), device = device)
        if count < 10:
            listofdata.append(new_data)
            count = count + 1
            #print(count)
        else:
            count = 0
            Data.objects.bulk_create(listofdata)
            print(listofdata)
            listofdata = []
        if count_del < 10:
            count_del = count_del + 1
        else:
            count_del = 0
            now = timezone.now()
            minut = timezone.timedelta(minutes=60)
            delta = (now - minut)
            print(delta)
            data_del = Data.objects.filter(createdAt__lt=delta).order_by('-createdAt')  #
            print(data_del)
            data_del.delete()

    def on_disconnect(client, userdata, rc):
        if rc != 0:
            sys.exit("Unexpected disconnection.")

    client.on_disconnect = on_disconnect
    client.subscribe(topic_sub)
    client.on_message = on_message
def mqtt_run():
    client = connect_mqtt()
    subscribe(client)
    publish(client, "'0.12'")
    client.loop_start()
def main():
    client = connect_mqtt()
    subscribe(client)
    #publish(client,"OK")
    client.loop_forever()
class Command(BaseCommand):
    def handle(self, *args, **options):
        #Data.objects.all().delete()
        main()
