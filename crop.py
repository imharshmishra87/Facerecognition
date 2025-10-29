import cv2 as cv
import numpy as np
img=cv.imread('images/image (1).jpg')

crop_img=img[0:600,0:600]
cv.imshow('cropped_image',crop_img)
cv.waitKey(0)

'''When put 0 as an origin the ihe origin of an image takes place from the left top corner'''
