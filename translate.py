import numpy as np
import cv2 as cv

'''positive X means shift to right, negative X means shift to left, positive Y means shift up and negative y means shift to down '''

def rescaling(frame,scale=None):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame,dim)

def translate(img,x,y):

    transmat=np.float32([[1,0,x],[0,1,y]])

    dim=(img.shape[0],img.shape[1])
    return rescaling(cv.warpAffine(img,transmat,dim),scale=0.50)

img=cv.imread('images/image (1).jpg')
shifted=translate(img,-100,-1000)
cv.imshow('shifted',shifted)
cv.waitKey(0)