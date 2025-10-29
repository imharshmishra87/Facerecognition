import cv2
import numpy as np

img=cv2.imread("image (1).jpg")
img2=cv2.imshow('image',img)
cv2.waitKey(0)
print(img2)

# Open cv cannot deal with images greater than computer dimension