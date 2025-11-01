import cv2 as cv
import numpy as np

def rescaling(frame,scale):
    height=int(frame.shape[1]*scale)
    width=int(frame.shape[0]*scale)
    dim=(height,width)

    return cv.resize(frame,dim)

img=cv.imread("faceregonition/images/image (1).jpg")
resized=rescaling(img,0.50)
cv.imshow('image',resized)
blank=np.zeros(resized.shape[:2],dtype='uint8')
cv.imshow('blank',blank)
mask=cv.circle(blank,(300,150),100,255,-1)
cv.imshow('circle',mask)

bitwisedimage=cv.bitwise_and(resized,resized,mask=mask)
cv.imshow('bitwised_image',bitwisedimage)

cv.waitKey(0)
cv.destroyAllWindows()