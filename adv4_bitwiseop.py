"""<So There are 4 major operators AND, OR, NOT, XOR, If the value of pixel is 0 then the pixel is turned off,
If the value of pixel is 1 then the pixel is turned on>"""

import cv2 as cv
import numpy as np

blank = np.zeros([400, 400], dtype="uint8")
rectangle = cv.rectangle(blank.copy(), (50, 50), (300, 300), 255, -1)
cv.imshow("rectangle", rectangle)
circle = cv.circle(blank.copy(), (200, 200), 150, 255, -1)
cv.imshow("circle", circle)

bitwise_and = cv.bitwise_and(rectangle, circle)
bitwise_or = cv.bitwise_or(rectangle, circle)
bitwise_not = cv.bitwise_not(circle)
bitwise_nor = cv.bitwise_xor(circle, rectangle)
cv.imshow("bitwise_or", bitwise_nor)
cv.waitKey(0)
