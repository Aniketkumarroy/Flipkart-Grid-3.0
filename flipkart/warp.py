import cv2 as cv
import numpy as np
img=cv.imread("C:\\Users\\ANIKET KUMAR ROY\\Desktop\\Programming\\Python\\OpenCV with Python\\flipkart\\6.jpeg")
img=cv.resize(img,(img.shape[1]//3,img.shape[0]//3))
cv.imshow("cards",img)
(h,w)=img.shape[:-1]
pt1=np.float32([[12,27],[526,27],[526,299],[12,299]])
pt2=np.float32([[0,0],[w,0],[w,h],[0,h]])
mat=cv.getPerspectiveTransform(pt1,pt2)
img2=cv.warpPerspective(img,mat,(w,h))

cv.imshow("output",img2)
print("ok")
cv.waitKey(0)
cv.destroyAllWindows()