import subprocess
import numpy as np
from rpi_car_manager import *

import time


def cam_detect():
   pass


def send2manager(client, msg2snt):
   # mqtt client
   tnow = time.localtime(time.time())
   msg = 'DSP_CAM Msg: ' + str(msg_device[3]) + ' at ' + time.asctime(tnow)

   client.publish(sub_topic[3], msg)
   print('message ' + msg + ' sent')
   pass

if __name__ == "__main__":
   cname = "Car_dsp_cam-"
   client = client_init(cname)
   try:
      while conn_time == 0:
         if cam_detect():
            send2manager(client,msg_device[3])
         print('send2manager procedure ended peacefully, next loop started')
   except KeyboardInterrupt:
      client.disconnect()  # disconnect from broker
      print("interrrupted by keyboard")
   finally: 
      client.disconnect()
