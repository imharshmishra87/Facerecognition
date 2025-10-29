import cv2
import numpy as np
img=cv2.imread('WIN_20251006_14_17_04_Pro.jpg')
img_resize1=cv2.resize(img,[400,600])
img_resize=cv2.imshow('imgage',img_resize1)
cv2.waitKey(0)
print(img_resize)

'''By functions'''

import cv2 as cv

def resizeimg(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    resize_image=cv.resize(frame,dimensions)
    resized=cv.imshow('resize',resize_image)
    print(resized)
    cv.waitKey(0)

frame1=cv.imread('images/image (1).jpg')
resizeimg(frame=frame1,scale=0.90)
cv.destroyAllWindows()
