import cv2 as cv
img=cv.imread("images/WIN_20251006_14_16_59_Pro.jpg")


def rescale(img,scale=None):
    width=int(img.shape[1]*scale)
    height=int(img.shape[0]*scale)
    dim=(width,height)

    return cv.resize(img,dim)
frame=rescale(img,scale=0.50)

# Average
blur=cv.blur(frame,(7,7))
cv.imshow('blurred_image',blur)

# Gaussian Blur
gs_blur=cv.GaussianBlur(frame,(7,7),0)
cv.imshow('gauss_blurred_image',gs_blur)

# Median Blur
md_blur=cv.medianBlur(frame,3)
cv.imshow('median_blur',md_blur)

# Bilateral Blur
bilateral=cv.bilateralFilter(frame,5,15,5)
cv.imshow('bilateral',bilateral)
# cv.imshow('image',frame)
cv.waitKey(0)

'''Averaging:- In this method of blurring the center pixel or middle piece of kernel box is calculated by calculating an average of surrounding pixels,

Gaussian Blur:- In this method the kernel pixels are assigned with some weight and the center kernel pixel is calculated as the avg of those weights and 
it is more natural provides less blur image then average blurring technique.

Median Blur:- Calculating the median of the intensity of the surrounding pixel. Performs better than average and gaussasian blur.

Bilateral Blur:- Basically blurs and retains the edges also.
'''