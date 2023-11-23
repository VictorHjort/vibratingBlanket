# Importing Libraries 
import serial 
import time 
import cv2
from ffpyplayer.player import MediaPlayer
import pandas as pd

arduino = serial.Serial(port='COM9', baudrate=115200, timeout=.1) 



data = pd.read_csv(r"C:\Users\Victor Hjort\Documents\TestSerial\src\clips\anger1\anger1.csv")
df = pd.DataFrame(data)
print(data)
intensity = df["Intensity"].values.tolist()
placement = df["Placement"].values.tolist()
when = df["Frame"].values.tolist()
print(placement)


def placementWithIntensity(intensityArray, placementArray):
    placeIntensityArray = []
    for count,i in enumerate(placementArray):
        if i == "LEFT":
            if intensityArray[count] == "OFF":
                placeIntensityArray.append('1')
            if intensityArray[count] == "LOW":
                placeIntensityArray.append('2')
            if intensityArray[count] == "MEDIUM":
                placeIntensityArray.append('3')
            if intensityArray[count] == "HIGH":
                placeIntensityArray.append('4')
        if i == "RIGHT":
            if intensityArray[count] == "OFF":
                placeIntensityArray.append('5')
            if intensityArray[count] == "LOW":
                placeIntensityArray.append('6')
            if intensityArray[count] == "MEDIUM":
                placeIntensityArray.append('7')
            if intensityArray[count] == "HIGH":
                placeIntensityArray.append('8')
        if i == "FRONT":
            if intensityArray[count] == "OFF":
                placeIntensityArray.append('9')
            if intensityArray[count] == "LOW":
                placeIntensityArray.append('10')
            if intensityArray[count] == "MEDIUM":
                placeIntensityArray.append('11')
            if intensityArray[count] == "HIGH":
                placeIntensityArray.append('12')
        if i == "BACK":
            if intensityArray[count] == "OFF":
                placeIntensityArray.append('13')
            if intensityArray[count] == "LOW":
                placeIntensityArray.append('14')
            if intensityArray[count] == "MEDIUM":
                placeIntensityArray.append('15')
            if intensityArray[count] == "HIGH":
                placeIntensityArray.append('16')
    return placeIntensityArray
    
def write_read(x): 
    arduino.write(bytes(x, 'utf-8')) 
    time.sleep(0.02) 
    data = arduino.readline() 
    return data 

def playVideo(fileName, frameChoice, placementAndIntensity):
    #creating video capture object
    cap = cv2.VideoCapture(fileName)
    #creating media player object
    player = MediaPlayer(fileName)
    #variable to keep control of framenumber
    frameNum = 1;
    #variable to keep control of the nexr array index
    arrayNum = 0;
    #variable for window name
    windowName = 'window'


    #Did camera open?
    if(cap.isOpened()==False):
        print("Error opening video file")
    
    #Setting the window to fullscreen
    cv2.namedWindow(windowName, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    #While loop until last frame
    while(cap.isOpened()):
        #Display the resulting frame and audio
        ret, frame = cap.read()
        audio_frame, val = player.get_frame()
        if ret == True:
            #Display resulting frame
            cv2.imshow(windowName, frame)
            #Printing framenumber for debugging
            print(frameNum)
            #If framenumber in dictionary send spot and intensity to microcontroller
            if val != 'eof' and audio_frame is not None:
                #audio
                img, t = audio_frame
            if frameNum in frameChoice:
                print(write_read(placementAndIntensity[arrayNum]))
                arrayNum += 1
            frameNum += 1
            if cv2.waitKey(6) & 0xFF == ord('q'): 
                break
        else:
            break
    # When everything done, release 
    # the video capture object 
    cap.release() 

    # Closes all the frames 
    cv2.destroyAllWindows()


mainArray = placementWithIntensity(intensity, placement)
playVideo(r"C:\Users\Victor Hjort\Documents\TestSerial\src\clips\anger1\anger1.mp4", when, mainArray)

    


