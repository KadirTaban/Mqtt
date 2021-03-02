import paho.mqtt.client as paho
import time
broker="broker.emqx.io"
print("Broker(arabulucu,bağlayıcı) a bağlanıldı.")
port=1883

def on_publish(client,userdata,result):
    print("data published \n")
    pass

client1=paho.Client("Control") #İstemci(client) objesini oluştur

client1.connect("broker.emqx.io")#istemci(client)in bağlantısı
print("bağlantı kuruldu")
client1.loop_start()
client1.on_publish=on_publish#callback function çağrıldı

client1.connect(broker,port)#publish the message

ret=client1.publish("mountain/herbals","on")#on_publish kullanan yayın bilgisini incele.
time.sleep(10)
client1.loop_stop()