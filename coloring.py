import cv2 as cv
import numpy as np

blank=np.zeros([512,512,3])
blank[:300,:150]=0,258,0
img=cv.imshow('blank',blank)
cv.waitKey(0)