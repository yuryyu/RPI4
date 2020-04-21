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
        if msg_device in msg:
            print('Door opened!')
            if stranger():
                send_alarm(client)

def stranger():
    return True

def send_alarm(client):
    print("Sending alarm message")
    tnow=time.localtime(time.time())
    client.publish(pub_topic,time.asctime(tnow)+' Alarm! Penetration! Call to Police!')    

def main():    

    r=random.randrange(1,100000)
    ID="RPI4_-"+str(r)

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

    # main monitoring loop
    client.loop_start()  #Start loop
    client.subscribe(sub_topic)
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
