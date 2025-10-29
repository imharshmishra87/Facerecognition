import numpy as np
import cv2 as cv

def rescaling(frame,scale=0.50):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    dim=(width,height)

    return cv.resize(frame,dim)

img=cv.imread('images/image (1).jpg')



resized_img=rescaling(img)
canny2=cv.Canny(resized_img,125,175)
cv.imshow('image',canny2)
blur=cv.GaussianBlur(resized_img,(3,3),cv.BORDER_DEFAULT)
canny=cv.Canny(blur,125,175)
cv.imshow('image_with_blur',canny)
cv.waitKey(0)
