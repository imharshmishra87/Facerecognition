import cv2 as cv
import numpy as np
img=cv.imread("faceregonition/images/newfile.png")
cv.imshow('orgimage',img)
gray_image=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Binarising the value of the image 
# When the value of the pixel is greater than threshold than it turns white else black
threshold, thresh=cv.threshold(gray_image,205,255,cv.THRESH_BINARY)
cv.imshow('Threshold',thresh)
threshold, invthresh=cv.threshold(gray_image,205,255,cv.THRESH_BINARY_INV)
cv.imshow('invThreshold',invthresh)

# Adaptive Thresholding
adaptive_thresholding=cv.adaptiveThreshold(gray_image,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,0.01)
gadaptive_thresholding=cv.adaptiveThreshold(gray_image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,0.01)
cv.imshow('Adaptive',adaptive_thresholding) 
cv.imshow('gAdaptive',gadaptive_thresholding) 
cv.waitKey(0)