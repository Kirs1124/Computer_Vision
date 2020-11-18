import numpy as np
import cv2
import matplotlib.pyplot as plt
img = np.zeros((300,300,3), dtype=np.uint8)
img[:,0:100,0] = 255
img[:,100:200,1] = 255
img[:,200:300,2] = 255
print("img=\n",img)
# plt.imshow(img)
# plt.show()
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()