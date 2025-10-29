import cv2 as cv
import numpy as np

def rescaling(frame,scale=0.50):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    dim=(width,height)

    return cv.resize(frame,dim)

img=cv.imread('images/image (1).jpg')
rescaledimg=rescaling(img)
blur=cv.GaussianBlur(rescaledimg,(3,3),cv.BORDER_DEFAULT)
cv.imshow('image',blur)
cv.waitKey(0)