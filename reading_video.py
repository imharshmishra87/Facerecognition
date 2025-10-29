import cv2 as cv
capture=cv.VideoCapture("videos\WIN_20251016_20_50_08_Pro.mp4")
while True:
    isTrue, frame=capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(40) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

'''Step1 -> We are reading video frame by frame
step2-> showing video by frame
step3-> When waitkey is 40 and 0xFF==ord('d') then break'''

'''End we are getting error because our open cv cant find more frame.'''