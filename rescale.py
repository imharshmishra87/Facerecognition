import cv2 as cv

def resolution(width,height):
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture(0)

while True:
    istrue,frame=capture.read()
    cv.imshow('rescaled',frame)

    if cv.waitKey(20) & 0XFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()