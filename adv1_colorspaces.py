'''Color spaces mainly refers to the array of color pixels. There exists multiple colour spaces such as BGR, GRAY, LAMB etc
HSV:- Hue Saturation'''
import matplotlib.pyplot as plt
import cv2 as cv
img=cv.imread('images/image (1).jpg')
(width,height)=int(img.shape[1]//2),int(img.shape[0]//2)
dim=(width,height)
resized=cv.resize(img,dim)

# Converting image to gray
gray_image=cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('gray_image',gray_image)

# Converting image to HS
hsv_image=cv.cvtColor(resized,cv.COLOR_BGR2HSV)
cv.imshow('hsv_image',hsv_image)

# Converting BGR image to LAMB
lamb_image=cv.cvtColor(resized,cv.COLOR_BGR2LAB)
cv.imshow('lamb_image',lamb_image)

# Converting BGR image to RGB
rgb=cv.cvtColor(resized,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
plt.imshow(rgb)
plt.show()
cv.waitKey(0)

# converting grayscale to hsv

gray_img=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow('Gray_image',gray_img)

lamb=cv.cvtColor(gray_img,cv.COLOR_GRAY2BGR)
hsv=cv.cvtColor(lamb,cv.COLOR_BGR2HSV)
cv.imshow('hsv_image',hsv)
cv.waitKey(0)

'''Note:-
1. We can convert gray to BGR(Reverse)
2. We can convert HSV to BGR(REverse)
3. We can convert lamb to BGR(Reverse)
4. We can convert BGR to RGB(Reverse)
we can not convert grayscale to hsv directly to do that first we need to convert gray scale to BGR and then to HSV'''
