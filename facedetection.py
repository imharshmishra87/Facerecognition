
import cv2 as cv
from retinaface import RetinaFace as rt
img=cv.imread("faceregonition/images/WIN_20251006_14_16_59_Pro.jpg")

def harcascade():
    haarcascade=cv.CascadeClassifier("faceregonition/haarcascade.xml")
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_data=haarcascade.detectMultiScale(gray,1.05, 3)
    # cv.imshow('blur',blur)

    for (x,y,w,h) in face_data:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    cv.imshow('facedetction',img)

    cv.waitKey(0)

def retinaface():
    image=rt.detect_faces(img)
    for i in image.keys():
        identity=image[i]
        faces=identity['facial_area']
        cv.rectangle(img,(faces[0],faces[1]),(faces[2],faces[3]),(0,0,255),2)
    cv.imshow('image',img)
    cv.waitKey(0)
print(retinaface())