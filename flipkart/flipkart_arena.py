import cv2 as cv
import numpy as np
# arena=np.zeros((600,1200,3),np.uint8)
# (h,w)=(arena.shape[0],arena.shape[1])
# cv.rectangle(arena,(8*w//20,0),(12*w//20,8*h//10),(255,255,255),-1)
# cv.rectangle(arena,(0,8*arena.shape[0]//10),(arena.shape[1],arena.shape[0]),(255,255,255),-1)
# for i in range(21):
#     cv.line(arena,(i*arena.shape[1]//20,0),(i*arena.shape[1]//20,arena.shape[0]),(0,0,0),1)
# cv.line(arena,(arena.shape[1]//20,8*arena.shape[0]//10),(arena.shape[1]//20,arena.shape[1]),(50,50,150),8)
# cv.line(arena,(19*arena.shape[1]//20,8*arena.shape[0]//10),(19*arena.shape[1]//20,arena.shape[0]),(50,50,150),8)
# for i in range(10):
#     cv.line(arena,(0, 60*i),(1200,60*i),(0,0,0),1)
# cv.rectangle(arena,(0,0),(420,420),(255,255,255),-1)
# cv.rectangle(arena,(780,0),(1200,420),(255,255,255),-1)
# arena=cv.resize(arena,(1900,800))
# cv.imshow("image",arena)
# cv.imwrite("C:\\Users\ANIKET KUMAR ROY\\Desktop\\Programming\\OpenCV-files\\arena.jpg",arena)
# ---------------------------------------
def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv.cvtColor(imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver
#---------------------------------------
arena=cv.imread("C:\\Users\ANIKET KUMAR ROY\\Desktop\\Programming\\OpenCV-files\\arena.jpg")
blank=np.zeros((300,600,3),np.uint8)
img=cv.resize(arena,(600,300))
mask1,mask2,mask3,mask4=blank.copy(),blank.copy(),blank.copy(),blank.copy()
mask4[30:240,330:360,:],mask4[240:270,330:600,:]=255,255
mask3[30:270,300:330,:],mask3[270:300,300:600,:]=255,255
mask2[30:270,270:300,:],mask2[270:300,0:300,:]=255,255
mask1[30:240,240:270,:],mask1[240:270,0:270,:]=255,255
track4=cv.bitwise_and(mask4,img)
track3=cv.bitwise_and(mask3,img)
track2=cv.bitwise_and(mask2,img)
track1=cv.bitwise_and(mask1,img)
cv.rectangle(track1,(4,2),(596,302),(0,255,0),2)
cv.putText(track1,"Track 1",(20,40),2,1,(255,0,0),2)
cv.rectangle(track2,(4,2),(596,302),(0,255,0),2)
cv.putText(track2,"Track 2",(20,40),2,1,(255,0,0),2)
cv.rectangle(track3,(4,2),(596,302),(0,255,0),2)
cv.putText(track3,"Track 3",(20,40),2,1,(255,0,0),2)
cv.rectangle(track4,(4,2),(596,302),(0,255,0),2)
cv.putText(track4,"Track 4",(20,40),2,1,(255,0,0),2)
imgstack=stackImages(1,[[track1,track2],[track3,track4]])
cv.imshow("stack image",imgstack)
cv.imshow("arena",arena)
cv.waitKey(0)
cv.destroyAllWindows()