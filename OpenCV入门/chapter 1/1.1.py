import cv2

lena = cv2.imread("lena.bmp")
print(lena)
cv2.namedWindow("lesson")
cv2.imshow("lesson", lena)
retval = cv2.waitKey(1000)
print(retval)