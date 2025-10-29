import cv2 as cv
import numpy as np

arr=np.zeros([512,512,3])
cv.rectangle(arr,(0,0),(420,420),(0,255,0),thickness=1)
cv.circle(arr,(250,250),10,(0,0,255),thickness=-1)
cv.line(arr,(0,0),(512,512),(0,0,255),thickness=1)
cv.putText(arr,'Hello My Name Is Harsh',(300,300),cv.FONT_HERSHEY_PLAIN,1.0,(0,0,255))
cv.imshow('blank',arr)
cv.waitKey(0)