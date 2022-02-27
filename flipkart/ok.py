import cv2 as cv2

def getContours(img):
     
    

    contours, hierarchy = cv2.findContours(img,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if (area > 10 and area < 200):
            approx = cv2.approxPolyDP(contour, 0.009 * cv2.arcLength(contour, True), True)
            cv2.drawContours(new_img, [approx], 0, (0, 0, 255), 5)
            x,y,w,h=cv2.boundingrect(approx)
            cv2.circle(img2,(x+w//2,y+h//2),5,(0,0,255),-1)
            cv.imshow("track",img2) 


cap=cv2.videocapture(0)
while True:
    ret,frame=cap.read()
    frame=img
    hsv_frame = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)
    low_green=np.array([25,52,72])
    high_green=np.array([102,255,255])
    green_mask=cv2.inRange(hsv_frame,low_green,high_green)
    green=cv2.bitwise_and(new_img,new_img,mask=green_mask)

    kernel = np.ones((7, 7), np.uint8)
    img_erosion = cv2.erode(green_mask, kernel, iterations=2)