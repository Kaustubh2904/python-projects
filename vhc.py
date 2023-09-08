import cv2
import time 
import time 
import numpy as np 
import hand_module as htm
import math
import pycaw
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


####################################
wCam, hcam = 640,480
#####################################



cap= cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hcam)
pTime = 0 
cTime = 0 
detector = htm.handDetector(detectioncon=0.7)  #we change the detection con so that it can be smoother and some other things are not detected 

devices = AudioUtilities.GetSpeakers()                     #from here 
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)  #till here is the initialization of this pycaw 
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400 # because 400 == 0 and at start it should be at 0
volPer = 0 

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList= detector.findPos(img, draw = False)
    if len(lmList) != 0:
        #print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 =lmList[8][1], lmList[8][2] 
        cx, cy = ((x1+x2)//2) , ((y1+y2)//2)

        cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED ) 
        cv2.circle(img, (x2,y2), 15, (255,0,255), cv2.FILLED )
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255), 3 )
        cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED )

        length = math.hypot(x2-x1, y2-y1)
        #print(length)

        #our hand range was 300 max to 50 min this is to be converted to volume range i.e. -65 to 0 
        # we can use numpy for this 

        vol= np.interp(length, [50,300], [minVol,maxVol])#play around to make it smoother
        volBar= np.interp(length, [50,300], [400,150])  #400 is where 0volume and 150 is where volume 100 will be 
        volPer= np.interp(length, [50,300], [000,100])#this is for % of volume 
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx,cy), 15, (0,255,0), cv2.FILLED)


    cv2.rectangle(img,(50,150), (85,400), (0,255,0), 3)
    cv2.rectangle(img,(50, int(volBar)), (85,400), (0,255,0), cv2.FILLED) #85-3- this is bascially 2d coordinate system kinda things and then the color 
    cv2.putText(img, f'{int(volPer)} % ', (40,450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255  ,0), 3)



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime= cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0,0), 3)

    cv2.imshow ("IMG", img)
    key = cv2.waitKey(1)

    if key== ord('q'):
        break  