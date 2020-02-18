import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")

def on_message(client, userdata, message):
    print ("Message recieved: " + str(message.payload.decode("utf-8")))
 
Connected = False   #global variable for the state of the connection
 
broker_address= "10.42.12.200"
port = 1883

client = mqttClient.Client()               #create new instance   #set username and password
client.on_connect = on_connect
client.on_message = on_message #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe("temperature")

try:
    while True:
        time.sleep(1);
except KeyboardInterrupt:
    print ("Exiting")
    client.disconnect()
    client.loop_stop()
 

try:
    while True:
 
        value = input('Enter the message:')
        client.publish("temperature",value)
 
except KeyboardInterrupt:
 
    client.disconnect()
    client.loop_stop()



    
