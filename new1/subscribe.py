import paho.mqtt.client as mqtt
import time

def callback(client,userdata,message):
    print("message received",str(message.payload.decode("utf-8")))
    print("message topic",message.topic)
    print("message qos",message.qos)
    print("message retain flag=",message.retain)

broker_address="broker.emqx.io"
print("creating new instance")
client=mqtt.Client("Sub")
client.callback=callback
print("connecting to broker")
client.connect(broker_address)
client.loop_start()
print("subscribing to topic","mountains/trees")
client.subscribe("mountains/trees")
print("Publishing message to topic","mountains/trees")
client.publish("mountains/tress","OFF")
time.sleep(10)
client.loop_stop()

