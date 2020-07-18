
import socket

nb=1 # 0- HIT-"139.162.222.115", 1 - open HiveMQ - broker.hivemq.com
brokers=[str(socket.gethostbyname('vmm1.saaintertrade.com')), str(socket.gethostbyname('broker.hivemq.com'))]
ports=[80,1883]
usernames = ['',''] # should be modified for HIT
passwords = ['',''] # should be modified for HIT
broker_ip=brokers[nb]
port=ports[nb]
username = usernames[nb]
password = passwords[nb]
conn_time = 0 # 0 stands for endless
mzs=['matzi/','']
sub_topic = [mzs[nb]+'car/engine/status', mzs[nb]+'car/belt/status', mzs[nb]+'car/THD', mzs[nb]+'DSP/Camera/status', mzs[nb]+'DSP/UltraS/status', mzs[nb]+'DSP/Mic/status']
msg_device = ['stopped', 'opened', 'hot', 'detected']
pub_topic = mzs[nb]+'car/system/state'
msg_system = ['Possibly Child in the auto!', 'Very hot in the auto!', 'Childs Belt opened!']
isplot = False
issave = True
# define crop coordinates from RPI cam taken image 2464 x 3280:
y0=902
x0=1012
y1=2262
x1=2052

# DSP thresholds
# sound (mic module)
mic_thrh = 2.4
# ultrasound distance to back seat (cm)
US_thrh = 120.00
# RPI camera detection thresholds
deviation_percentage = 15
max_eucl = 0.5

threshold = [0.0, 0.06265732, 0.12531464, 0.18797196, 0.25062928, 0.3132866,
 0.37594393, 0.43860126, 0.50125855, 0.5639159 , 0.6265732 , 0.6892305,
 0.75188786, 0.81454515, 0.8772025,  0.9398598 , 1.0025171 , 1.0651745,
 1.1278318,  1.190489 ,  1.2531464 , 1.3158038 , 1.378461 ,  1.4411184,
 1.5037757,  1.566433 ,  1.6290903,  1.6917477 , 1.754405  , 1.8170623,
 1.8797196 ]