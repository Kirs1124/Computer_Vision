import cv2
import numpy as np

img1 = np.ones((4, 4), dtype=np.uint8) * 3
img2 = np.ones((4, 4), dtype=np.uint8) * 5
mask = np.zeros((4, 4), dtype=np.uint8)
mask[2:4, 2:4] = 1
img3 = np.ones((4, 4), dtype=np.uint8) * 66
print("img1=", img1)
print("img2=", img2)
print("mask=", mask)
print("初始值img3=", img3)
img3 = cv2.add(img1, img2, mask=mask)
print("求和后img3=", img3)
