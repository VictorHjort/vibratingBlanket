# importing libraries 
import cv2 
import numpy as np 
import serial.tools.list_ports
import time

#Declaring variables
#Port variables
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []
#Vibration variables
intnesity = ['OFF','LOW','MEDIUM','HIGH']


def choosePort():
 for onePort in ports:
  portsList.append[onePort]
 val = input("Select port: COM")
 print("Chosen port: COM" + str(val))
 for x in range(0, len(portsList)):
  if portsList[x].starswith("COM" + str(val)):
   portVar = "COM" + str(val)
 return portVar

def playVideo(fileName):
    # Create a VideoCapture object and read from input file 
	cap = cv2.VideoCapture(fileName) 
	frameNum = 0;

	# Check if camera opened successfully 
	if (cap.isOpened()== False): 
		print("Error opening video file") 

	#Start time measure
	startTime = time.time()
	# Read until video is completed 
	while(cap.isOpened()): 
		
	# Capture frame-by-frame 
		ret, frame = cap.read() 
		if ret == True: 
		# Display the resulting frame 
			cv2.imshow('Frame', frame) 
			print(frameNum)
			frameNum += 1
			nowTime = time.time()
			if nowTime - startTime > 1:
				print("1 second")
				startTime = time.time()
				frameNum = 0
		# Press Q on keyboard to exit 
			if cv2.waitKey(25) & 0xFF == ord('q'): 
				break

	# Break the loop 
		else: 
			break

	# When everything done, release 
	# the video capture object 
	cap.release() 

	# Closes all the frames 
	cv2.destroyAllWindows()

def sendCommand(vibrationIntensity):
    	

serialInst.baudrate = 9600
serialInst.port = choosePort()
serialInst.open()


playVideo("world.mp4")