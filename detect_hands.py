import cv2 #this is for visulaization
import mediapipe as mp #this is for hand detection 
import time #this is for fps and time interval things not particularly used in this code 
# Create a VideoCapture object to access the webcam (0 represents the default camera)
cap = cv2.VideoCapture(0)


#Initialize mediapipe components for hand tracking:
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils 

#to contineously capture and display frames 
while True :
    #Capture a frame from the webcam:cap.read() reads a frame from the webcam, and success is a Boolean indicating whether the frame was successfully captured. img holds the captured frame.

    success, img = cap.read()

    #Convert the captured frame to RGB format:
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    #Process the frame to detect hands:
    results = hands.process(imgRGB)

#Check if any hands were detected in the frame
    if results.multi_hand_landmarks:

        #If hands were detected, loop through the landmarks and draw them on the frame:
        for handlmks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handlmks,mpHands.HAND_CONNECTIONS)


# Display the processed frame with landmarks
    cv2.imshow("image", img)
    #key variable has an object cv2.waitkey which checks for any key oresses to exit the video capture thing 
    key = cv2.waitKey(1)
    if key == ord('q'):
        break 
