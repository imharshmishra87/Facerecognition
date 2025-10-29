import cv2
import numpy as np
img=cv2.imread('images/image (1).jpg')
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
image_gray=cv2.imshow('gray_image',gray_image)
cv2.waitKey(0)
print(image_gray)
