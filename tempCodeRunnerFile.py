    cv2.rectangle(img,(50,150), (85,400), (0,255,0), 3)
        cv2.rectangle(img,(50, int(volBar)), (85,400), (0,255,0), cv2.FILLED) #85-3- this is bascially 2d coordinate system kinda things and then the color 
        cv2.putText(img, f'{int(volPer)} % ', (40,450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255  ,0), 3)