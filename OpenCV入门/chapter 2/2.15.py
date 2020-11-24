import numpy as np
import cv2
lena = cv2.imread("../chapter 3/lena512.bmp", cv2.IMREAD_UNCHANGED)
dollar = cv2.imread("../chapter 3/dollar.bmp", cv2.IMREAD_UNCHANGED)
cv2.imshow("lena", lena)
cv2.imshow("dollar", dollar)
face = lena[220:400, 250:350]
dollar[160:340, 200:300] = face
cv2.imshow("after_dollar", dollar)
cv2.waitKey()
cv2.destroyAllWindows()