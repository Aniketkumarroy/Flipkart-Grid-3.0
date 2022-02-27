import cv2 as cv
import numpy as np


def click(event,x,y,flags,params):
    if event==cv.EVENT_LBUTTONDOWN:
        p.append([x,y])
    elif event==cv.EVENT_RBUTTONDOWN:
        l.append([x,y])


def track(img,arr1,arr2,lower=[60,173,14],upper=[95,255,255]):
    lower=np.array(lower)
    upper=np.array(upper)
    imghsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    mask=cv.inRange(imghsv, lower, upper)
    tracking=cv.bitwise_and(img,img,mask=mask)
    cv.polylines(tracking,[arr1],True,(255,0,0),1)
    cv.polylines(tracking,[arr2],False,(0,0,255),2)
    cv.imshow("Tracking",tracking)


path="C:\\Users\\ANIKET KUMAR ROY\\Desktop\\Programming\\Python\\OpenCV with Python\\flipkart\\3.jpeg"
img=cv.imread(path)
img=cv.resize(img,(img.shape[1]//3,img.shape[0]//3))
p=[]
l=[]

while True:
    # img=cv.resize(img,(img.shape[1]//3,img.shape[0]//3))
    cv.imshow("original",img)
    cv.imshow("window",img)
    cv.setMouseCallback("window",click)
    if len(p)%6==0 and len(p) and len(l)%3==0 and len(l):
        mask=np.zeros(img.shape,np.uint8)
        arr1=np.array(p[-6:])
        arr2=np.array(l[-3:])
        cv.fillPoly(mask,[arr1],(255,255,255))
        output=cv.bitwise_and(img,mask)
        track(output,arr1,arr2)
        cv.imshow("out",output)
    key=cv.waitKey(1)
    if key& 0xFF==ord('c'):
        p=[]
        img=cv.imread(path)
        img=cv.resize(img,(img.shape[1]//3,img.shape[0]//3))
    if key &0xFF==ord('q'):
        break
cv.destroyAllWindows()