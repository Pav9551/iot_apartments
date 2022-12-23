#from paho.mqtt import client as mqtt_client
import paho.mqtt.client as mqtt_client
import json
#broker = '79.174.12.210'
broker = '78.24.223.130'
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
            ("coridor1/sensor/#", 0),
            ("coridor2/sensor/#", 0),
             ]
# generate client ID with pub prefix randomly
client_id = '123'
username = 'mqtt_user'
password = 'mqtt_user'
deviceId = "1"

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
        print(f"Recieved '{msg.payload.decode()}' from '{msg.topic}' topic")
        #publish(client, "'0.12'")
        #y = json.loads(msg.payload.decode())
        #temp = y["notification"]["parameters"]["temp"]
        #hum = y["notification"]["parameters"]["humi"]
        #print("temperature: ",temp,", humidity:",hum)
    client.subscribe(topic_sub)
    client.on_message = on_message

def mqtt_run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
def main():
    client = connect_mqtt()
    subscribe(client)
    #publish(client,"OK")
    client.loop_forever()
print(__name__)
if __name__ == '__main__':
    main()

