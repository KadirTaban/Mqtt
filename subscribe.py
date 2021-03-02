import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):#here is callback function
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
broker_address="broker.emqx.io"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P2") #create new instance
client.on_message=on_message #attach function to callback for faster procces
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","on")
time.sleep(10) # wait
client.loop_stop() #stop the loop
#QoS : At most once (0)At least once (1)Exactly once (2).