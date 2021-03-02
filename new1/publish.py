import paho.mqtt.client as mqtt
broker_address="broker.emqx.io"
client=mqtt.Client("Publish_1")
client.connect(broker_address)
client.publish("mountain/trees","OFF")