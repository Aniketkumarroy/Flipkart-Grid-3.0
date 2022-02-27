import cv2 as cv
img=cv.imread("C:\\Users\\ANIKET KUMAR ROY\\Videos\\Captures\\CoppeliaSim Edu - task_2a - rendering_ 5 ms (7.9 fps) - SIMULATION STOPPED 12-11-2021 01_22_11.png")
img=cv.resize(img,(img.shape[1]//3,img.shape[0]//3))
imghsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
box=cv.selectROI("test",img,False)
print(box)
# mat=imghsv[box[1]:box[1]+box[3],box[0]:box[0]+box[2]]
print(img[box[1]:box[1]+box[3],box[0]:box[0]+box[2]])
# hue_min=mat[mat[:,:,0].argmin()]
cv.waitKey(0)
cv.destroyAllWindows()