import cv2 as cv
def rescalevideo(frame,scale=0.50):
    # This will wrok for images, videos and live videos.
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture('videos/WIN_20251016_20_50_08_Pro.mp4')

while True:
    istrue, frame= capture.read()

    resized_frame=rescalevideo(frame)
    cv.imshow('frame',resized_frame)

    if cv.waitKey(40) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

