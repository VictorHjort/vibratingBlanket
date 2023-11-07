# importing libraries 
import cv2 
import numpy as np 
import serial
import time

#This is for sending serial information to the teensy
#teensy = serial.Serial(port="COM4", baudrate=115200, timeout=.1)
 
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
def sendSerial(intensity):