
import socket

nb=0 # 0- HIT-"139.162.222.115", 1 - open HiveMQ - broker.hivemq.com
brokers=[str(socket.gethostbyname('vmm1.saaintertrade.com')), str(socket.gethostbyname('broker.hivemq.com'))]
ports=[80,1883]
usernames = ['MATZI',''] # should be modified for HIT
passwords = ['MATZI',''] # should be modified for HIT
broker_ip=brokers[nb]
port=ports[nb]
username = usernames[nb]
password = passwords[nb]
conn_time = 0 # 0 stands for endless
mzs=['matzi/','']
sub_topic = [mzs[nb]+'car/engine/status', mzs[nb]+'car/belt/status', mzs[nb]+'car/THD', mzs[nb]+'DSP/Camera/status', mzs[nb]+'DSP/UltraS/status', mzs[nb]+'DSP/Mic/status']
msg_device = ['stopped', 'opened', 'hot', 'detected', 'detected', 'detected']
pub_topic = mzs[nb]+'car/system/state'
msg_system = ['Possibly Child in the auto!', 'Very hot in the auto!', 'Childs Belt opened!']
