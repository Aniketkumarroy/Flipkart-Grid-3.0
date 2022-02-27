import cv2 as cv
import numpy as np
path="C:\\Users\\ANIKET KUMAR ROY\\Desktop\\Programming\\Python\\OpenCV with Python\\flipkart\\3.jpeg"

img=cv.imread(path)
img=cv.resize(img,(img.shape[1]//3,img.shape[0]//3))
# box=cv.selectROI("test",img,False)
# imghsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# print(box)
# mat=imghsv[box[1]:box[1]+box[3],box[0]:box[0]+box[2]]
# print(mat)
# print(mat[:,:,0].argmin())
# h_min=mat[mat[:,:,0].argmin()]
# h_max=mat[mat[:,:,0].argmax()]
# sat_min=mat[mat[:,:,1].argmin()]
# sat_max=mat[mat[:,:,1].argmax()]
# val_min=mat[mat[:,:,2].argmin()]
# val_max=mat[mat[:,:,2].argmax()]



cv.namedWindow("trackbar")
cv.resizeWindow("trackbar",640,240)
def empty(x):
    pass
cv.createTrackbar("hue min","trackbar",60,179,empty)
cv.createTrackbar("hue max","trackbar",95,179,empty)
cv.createTrackbar("sat min","trackbar",173,255,empty)
cv.createTrackbar("sat max","trackbar",255,255,empty)
cv.createTrackbar("val min","trackbar",14,255,empty)
cv.createTrackbar("val max","trackbar",255,255,empty)
while True:
    img=cv.imread(path)
    img=cv.resize(img,(img.shape[1]//3,img.shape[0]//3))
    imghsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    h_min=cv.getTrackbarPos("hue min","trackbar")
    h_max=cv.getTrackbarPos("hue max","trackbar")
    sat_min=cv.getTrackbarPos("sat min","trackbar")
    sat_max=cv.getTrackbarPos("sat max","trackbar")
    val_min=cv.getTrackbarPos("val min","trackbar")
    val_max=cv.getTrackbarPos("val max","trackbar")
    lower=np.array([h_min,sat_min,val_min])
    upper=np.array([h_max,sat_max,val_max])
    mask=cv.inRange(imghsv,lower,upper)
    cv.imshow("mask",mask)
    output=cv.bitwise_and(img,img,mask=mask)
    cv.imshow("original",img)
    cv.imshow("output",output)
    if cv.waitKey(1)&0xFF==ord('q'):
        break
# cv.waitKey(0)
cv.destroyAllWindows()