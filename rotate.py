import cv2 as cv
import numpy as np
img=cv.imread('images/image (1).jpg')

'''When 0 flips the images vertically'''
flip=cv.flip(img,0)

'''Flips the image horizontally'''
flip=cv.flip(img,1)

'''Combined effect of both horizontal and vertical flip'''
flip=cv.flip(img,-1)

imgf=cv.imshow('image',flip)
cv.waitKey(0)

def rescaled(img,scale=0.50):
    width=int(img.shape[1]*scale)
    height=int(img.shape[0]*scale)

    dim=(width,height)
    return cv.resize(img,dim)


def rotateimage(src,angle,rot_point=None):
    (height,width)=src.shape[:2]

    if rot_point is None:
        rot_point=(width//2,height//2)

    rotmat=cv.getRotationMatrix2D(rot_point,angle,scale=1.0)

    dim=(width,height)
    return cv.warpAffine(src,rotmat,dim)

rotated=rotateimage(rescaled(img),30)
cv.imshow('Rotated',rotated)
cv.waitKey(0)

