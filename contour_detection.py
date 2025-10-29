"""Contours are the boundaries of an object which mainly helps in object detection and shape analysis it is different from edges
Threshold Means we are simply binarising the image say t1=125 and t2=250 then image pixel whose density is below t1 is marked 0 and above t2 is marked is as 1"""

import cv2 as cv
import numpy as np


img = cv.imread("images/image (1).jpg")
dim = (int(img.shape[1] // 2), int(img.shape[0] // 2))

resized = cv.resize(img, dim)

blank=np.zeros(resized.shape)
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

blured_img = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)

canny = cv.Canny(blured_img, 125, 175)
cv.imshow("image", canny)

# ret, thresh=cv.threshold(blured_img,125,250,cv.THRESH_BINARY)
# cv.imshow("image", thresh)
contours, heirarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('contours',blank)
print(len(contours))
cv.waitKey(0)
