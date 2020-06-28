
import socket

nb=1 # 0- HIT-"139.162.222.115", 1 - open HiveMQ - broker.hivemq.com
brokers=[str(socket.gethostbyname('vmm1.saaintertrade.com')), str(socket.gethostbyname('broker.hivemq.com'))]
ports=[80,1883]
usernames = ['','']
passwords = ['','']
broker_ip=brokers[nb]
port=ports[nb]
username = usernames[nb]
password = passwords[nb]
conn_time = 0 # 0 stands for endless
conn_time = 0 # 0 stands for endless
sub_topic = ['car/engine/status', 'car/belt/status', 'car/THD','DSP/Camera/status', 'DSP/UltraS/status','DSP/Mic/status']
msg_device = ['stopped', 'opened', 'hot', 'detected', 'detected', 'detected']
pub_topic = 'car/system/state'
