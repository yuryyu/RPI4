import subprocess
import numpy as np
from rpi_car_manager import *

import time





def send2manager(client, comp):
   # mqtt client
   tnow = time.localtime(time.time())
   msg = 'Watcher Msg: ' + str(comp) + ' at ' + time.asctime(tnow)

   client.publish(sub_topic[1], msg)
   print('message ' + msg + ' sent')
   pass

if __name__ == "__main__":
   cname = "RPI3_watcher-"
   client = client_init(cname)
   try:
      while conn_time == 0:
         
         print('send2manager procedure ended peacefully, next loop started')
   except KeyboardInterrupt:
      client.disconnect()  # disconnect from broker
      print("interrrupted by keyboard")
   finally: 
      client.disconnect()
