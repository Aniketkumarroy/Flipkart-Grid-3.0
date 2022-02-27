import cv2 as cv
import numpy as np
cap=cv.VideoCapture(2)
cap.set(3,600)
cap.set(4,1200)
while True:
    success,img=cap.read()
    blank=np.zeros(img.shape,np.uint8)
    cannyimg=cv.Canny(img,120,180)
    contours,hier=cv.findContours(cannyimg,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    #max_area=contours[0]
    for cnt in contours:
        if cv.contourArea(cnt)>cv.contourArea(max_area):
            max_area=cnt 
        cv.drawContours(blank,cnt,-1,(255,0,0),1)
    print(f"{len(contours)}")
    cv.imshow("video",blank)
    if cv.waitKey(10)&0xFF==ord('q'):
        break
cv.destroyAllWindows()