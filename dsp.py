import subprocess
import numpy as np
from rpi_car_manager import *
from mic import *
from ultrasound import *
import time


def cam_detect():
   pass

def US_detect():
   pass


def send2manager(client, msg2snt):
   # mqtt client
   tnow = time.localtime(time.time())
   msg = 'DSP_CAM Msg: ' + msg2snt + ' at ' + time.asctime(tnow)

   client.publish(sub_topic[3], msg)
   print('message ' + msg + ' sent')
   pass


def dsp_main():
   cname = "Car_dsp-"
   client = client_init(cname)
   try:
      while conn_time == 0:
         fname = 'data/cry/test_01.wav'

         if cam_detect() or mic_main(fname) > mic_thrh or US_detect() < US_thrh:
            send2manager(client, msg_device[3])         
         print('send2manager procedure ended peacefully, next loop started')       

   except KeyboardInterrupt:
      client.disconnect()  # disconnect from broker
      print("interrupted by keyboard")
   finally: 
      client.disconnect()

if __name__ == "__main__":
   dsp_main()