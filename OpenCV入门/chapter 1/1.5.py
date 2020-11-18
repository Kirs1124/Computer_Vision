import cv2

lena = cv2.imread("lena.bmp")
cv2.imshow("demo", lena)
cv2.waitKey()
cv2.destroyWindow("demo")
