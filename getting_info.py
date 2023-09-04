import cv2
import mediapipe as mp 
import time #this is for fps and time interval things not particularly used in this code 

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils 


pTime = 0 
cTime = 0 

while True :
   
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)


    if results.multi_hand_landmarks:
        for handlmks in results.multi_hand_landmarks:
            for id, lm in enumerate(handlmks.landmark):
                # print(id,lm)      //this gives decimal vlaues 
                h,w,c = img.shape   #this is an object of img class c is for channel
                cx, cy = int(lm.x*w), int(lm.y*h)  #here we are getiing pixel values of the lm.x and lm.y 
                print(id, cx, cy)
                
            mpDraw.draw_landmarks(img, handlmks,mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = (1/(cTime-pTime))   
    pTime = cTime 

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0,255), 3) #this displays fps @ img as str which has int values at position 10,70 aat some font with scale 3 color purple and thickness 3 

   
   
    cv2.imshow("image", img)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break 
