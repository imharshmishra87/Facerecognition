import numpy as np
import cv2 as cv
img=cv.imread("images/image (1).jpg")
width,height=int(img.shape[1]//2),int(img.shape[0]//2)
dim=(width,height)
resized=cv.resize(img,dim)

blank=np.zeros(resized.shape[:2])
circle=cv.circle(blank.copy(),(resized.shape[1]//2,resized.shape[0]//2),100,255,-1)

cv.waitKey(0)