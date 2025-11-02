import numpy as np
import cv2 as cv
from retinaface import RetinaFace as rt
capture=cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
# haarcascade=cv.CascadeClassifier('faceregonition\haarcascade.xml')
while True:
    isTrue,frame=capture.read()
    small=cv.resize(frame,(480,360))
    detect_face=rt.detect_faces(small)
    for i in detect_face.keys():
        identity=detect_face[i]
        data=identity['facial_area']
        cv.rectangle(frame,(data[0],data[1]),(data[2],data[3]),(0,255,0),2)
    cv.imshow('images',frame)
    

    # detect_face=haarcascade.detectMultiScale(grayframe,scaleFactor=1.15,minNeighbors=3)
    

    if cv.waitKey(40) and 0XFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()