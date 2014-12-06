#coding=utf-8

import cv2
import numpy as np

img = cv2.imread("3.jpg", 0)

gray_lap = cv2.Laplacian(img,cv2.CV_16S,ksize = 3)
dst = cv2.convertScaleAbs(gray_lap)

cv2.imshow('laplacian',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()