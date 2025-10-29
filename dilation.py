import cv2 as cv
def rescaling(frame,scale=None):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame,dim)
frame=cv.imread('images/image (1).jpg')
recaled_img=rescaling(frame,scale=0.50)

canny=cv.Canny(recaled_img,125,175)
cv.imshow('canny_image',canny)

dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilated_image',dilated)

eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('eroded_image',eroded)
cv.waitKey(0)
