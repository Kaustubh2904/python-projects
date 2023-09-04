import cv2
import mediapipe as mp 
import time
import hand_module as hm




cap = cv2.VideoCapture(0)
pTime = 0 
cTime = 0 
detector = hm.handDetector()

while True :
    success, img = cap.read()
    img = detector.findHands(img)
    lmList =  detector.findPos(img)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = (1/(cTime-pTime))   
    pTime = cTime 

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0,255), 3) #this displays fps @ img as str which has int values at position 10,70 aat some font with scale 3 color purple and thickness 3 

    cv2.imshow("webcam", img)
        
    key = cv2.waitKey(1)
    if key == ord('q'):
        break 