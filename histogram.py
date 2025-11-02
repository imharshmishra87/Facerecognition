import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
class histograms:
    def __init__(self,img):
        self.img=img
    
    def grayhistogram(self):
        gray_image = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        blank = np.zeros(self.img.shape[:2], dtype="uint8")
        circle = cv.circle(blank, (250, 150), 150, 255, -1)
        bitwised_img = cv.bitwise_and(gray_image, gray_image, mask=circle)
        cv.imshow("masked", bitwised_img)
        cvt_hist = cv.calcHist([gray_image], [0], bitwised_img, [256], [0, 256])

        plt.title("Gray Scale Histogram")
        plt.xlabel("Number of bins")
        plt.plot(cvt_hist)
        plt.show()
        cv.imshow("gray_image", gray_image)
        cv.waitKey(0)

    def colourhistogram(self):
        blank=np.zeros(self.img.shape[:2],dtype='uint8')
        mask=cv.rectangle(blank,(100,20),(400,300),255,-1)
        masked=cv.bitwise_and(self.img,self.img,mask=mask)
        plt.title("Coloured Histogram")
        plt.xlabel("Number of bins")
        plt.xlim(0,256)
        cv.imshow('circle',masked)
        colors=['B','G','R']
        for i, col in enumerate(colors):
            cvt_hist=cv.calcHist([self.img],[i],mask,[256],[0,256])
            plt.plot(cvt_hist)
        plt.show()
        cv.waitKey(0)

if __name__=='__main__':
    img = cv.imread("faceregonition/images/newfile.png")
    hist=histograms(img)
    hist.grayhistogram()
    hist.colourhistogram()