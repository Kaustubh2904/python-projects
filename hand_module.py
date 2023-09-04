import cv2
import mediapipe as mp 
import time #this is for fps and time interval things not particularly used in this code 

class handDetector():

    def __init__(self, mode = False, MaxHands = 3, complexity=1, detectioncon= 0.5 ,trackcon=0.5):  
        self.mode = mode
        self.MaxHands = MaxHands
        self.detectioncon= detectioncon
        self.trackcon= trackcon
        self.complexity = complexity 


        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.MaxHands, self.complexity, self.detectioncon,self.trackcon)
        self.mpDraw = mp.solutions.drawing_utils 


    def findHands(self, img, draw= True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handlmks in self.results.multi_hand_landmarks:
                if draw:
                     self.mpDraw.draw_landmarks(img, handlmks,self.mpHands.HAND_CONNECTIONS)
                    

        return img 


    def findPos(self, img, handNum = 0, draw = True):
        lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNum]
            for id, lm in enumerate(myHand.landmark):
                h,w,c = img.shape
                cx ,cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy), 10, (255,0,255), cv2.FILLED)
        return lmList


def main():
    cap = cv2.VideoCapture(0)
    pTime = 0 
    cTime = 0 
    detector = handDetector()

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

if __name__ == "__main__":
    main()
