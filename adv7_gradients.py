import numpy as np
import cv2 as cv

img=cv.imread("faceregonition/images/newfile.png")
gray_image=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Laplacian
lap=cv.Laplacian(gray_image,cv.CV_32F)
lap=np.uint8(np.absolute(lap))

'''The first lap line maily invloves calculating the pixel intensity difference by subtracting the left and right pixel values, these values can be either
negaive or positve and cv_64F preserves the data such as negative value.
The second line mainly converts the 64F into uint8 and absolute value is calculated.The decimal points are removed'''
cv.imshow('laplacian',lap)

# Sobel Method
sobelx=cv.Sobel(gray_image,cv.CV_64F,1,0)
sobely=cv.Sobel(gray_image,cv.CV_64F,0,1)
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
combined=cv.bitwise_or(sobelx,sobely)
cv.imshow('combined',combined)

# Canny edge detection

canny=cv.Canny(gray_image,155,250)
cv.imshow('cannyedge',canny)
cv.waitKey(0)