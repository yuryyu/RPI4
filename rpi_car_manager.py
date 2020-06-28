import paho.mqtt.client as mqtt
import os
import time
import sys, getopt
import logging
import queue
import random
from rpi_init import *

def on_log(client, userdata, level, buf):
    print("log: "+buf)
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
def on_disconnect(client, userdata, flags, rc=0):
    print("DisConnected result code "+str(rc))
def on_message(client,userdata,msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    process_message(client,m_decode,topic)
    print(m_decode)
    
def process_message(client,msg,topic):
    print("message processed: ",topic,msg)
    for ms in msg_device:
        if ms in msg:
            send_msg(client, pub_topic, msg)
            
def send_msg(client, topic, message):
    print("Sending message: " + message)
    tnow=time.localtime(time.time())
    client.publish(topic,time.asctime(tnow) + message)   

def client_init(cname):
    r=random.randrange(1,100000)
    ID=cname+str(r)

    client = mqtt.Client(ID, clean_session=True) # create new client instance
    # define callback function
    client.on_connect=on_connect  #bind call back function
    client.on_disconnect=on_disconnect
    client.on_log=on_log
    client.on_message=on_message

    if username !="":
        client.username_pw_set(username, password)        
    print("Connecting to broker ",broker_ip)
    client.connect(broker_ip,port)     #connect to broker
    return client

def main():    
    cname = "Car_Manager-"
    client = client_init(cname)

    # main monitoring loop
    client.loop_start()  #Start loop
    for tp in sub_topic:
        client.subscribe(tp)
    try:
        while conn_time==0:
            pass
        time.sleep(conn_time)
        
        print("con_time ending") 
    except KeyboardInterrupt:
        client.disconnect() # disconnect from broker
        print("interrrupted by keyboard")

    client.loop_stop()    #Stop loop
    # end session
    client.disconnect() # disconnect from broker
    print("End manager run script")

if __name__ == "__main__":
    main()
