import cv2
import numpy as np
img = cv2.imread('Car.jpg', 0)
cv2.imshow('car', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Car.png', img)