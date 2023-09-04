import cv2
import mediapipe as mp 
import time 
# Create a VideoCapture object to access the webcam (0 represents the default camera)
cap = cv2.VideoCapture(0)

#to cintineously capture and display frames 
while True :
    success, img = cap.read()

    cv2.imshow("image", img)
    #key variable has an object cv2.waitkey which checks for any key oresses to exit the video capture thing 
    key = cv2.waitKey(1)
    if key == ord('q'):
        break 

