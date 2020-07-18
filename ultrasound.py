#!/usr/bin/python

# run it by typing in terminal:
# python3 ultrasonic.py 23 24

import time, sys, os
import RPi.GPIO as GPIO


# init GPIO
def initGPIO(ECHO=24,TRIGGER=23):
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(TRIGGER,GPIO.OUT)
	GPIO.setup(ECHO, GPIO.OUT)
	GPIO.output(ECHO, False)
	GPIO.setup(ECHO,GPIO.IN)

def measure():
	initGPIO()
	start = 0
	realstart = 0
	realstart = time.time()
	GPIO.output(TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(TRIGGER, False)
	start = time.time()
	while GPIO.input(ECHO)==0:
		start = time.time()
		Dif = time.time() - realstart
		if Dif > 0.2:
			print("Ultrasonic Sensor Timed out, Restarting.")
			time.sleep(0.4)
			main()
	while GPIO.input(ECHO)==1:
		stop = time.time()
	elapsed = stop-start
	distance = (elapsed * 36000)/2
	GPIO.cleanup()
	return distance

def main():
	
	try:
		while True:
			distance = measure()
			print("Distance to back seat is: %.1f" % distance)
			if distance>100.0:
				print('Sending message to RCM: Back seat is clear')
			else:
				print('Sending message to RCM: The back seat is occupied!')
			print('Next measure will occured with 30 sec')
			time.sleep(30)
	except KeyboardInterrupt:
		GPIO.cleanup()

if __name__ == "__main__":
	# See if they inputted at least 2 Variables.
	if len( sys.argv ) < 3:
		print("\n\nTo use, type\npython "+sys.argv[0] + " Trigger_pin Echo_pin\nThey both need to be BCM GPIO Numbers.\n")
		sys.exit()
	else:
		ECHO    = int(sys.argv[2])
		TRIGGER = int(sys.argv[1])    
	main()
