import cv2

img = cv2.imread("../chapter 3/lenacolor.png")
cv2.imshow("lena1", img)
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
img[:, :, 0] = 0
cv2.imshow("lenab2", img)
img[:, :, 1] = 0
cv2.imshow("lenab0g0", img)
cv2.waitKey()
cv2.destroyAllWindows()
