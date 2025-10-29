import cv2 as cv
import numpy as np


img=cv.imread("images/image (1).jpg")
width,height=int(img.shape[1]//2),int(img.shape[0]//2)
dim=(width,height)
resized=cv.resize(img,dim)

# Splitting Of an Image into individual colours
b,g,r=cv.split(resized)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


blank=np.zeros(resized.shape[:2],dtype='uint8')

blue_green=cv.merge([b,g,blank])
green_red=cv.merge([blank,g,r])
red_blue=cv.merge([b,blank,r])

# blue=cv.merge([b,blank,blank])
# green=cv.merge([blank,g,blank])
# red=cv.merge([blank,blank,r])

cv.imshow('blue_green',blue_green)
cv.imshow('green_red',green_red)
cv.imshow('red_blue',red_blue)

# Merging of an image back to it's original form
# merged=cv.merge([b,g,r])
# cv.imshow('merged',merged)
cv.waitKey(0)