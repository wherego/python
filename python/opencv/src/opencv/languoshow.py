#coding=utf-8
import cv2
import numpy as np


img = cv2.imread('luoguo.jpg')

img2 = cv2.imread('30.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # 转成灰度图像
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) #将灰度图像转成二值图像

contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # 查找轮廓
cv2.drawContours(img,contours,-1,(0,0,255),3)

cv2.imshow("img", img)
cv2.waitKey(0)

gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)  # 转成灰度图像
ret2, binary2 = cv2.threshold(gray2,127,255,cv2.THRESH_BINARY) #将灰度图像转成二值图像

contours2, hierarchy2= cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # 查找轮廓
cv2.drawContours(img2,contours2,-1,(0,0,255),3)

cv2.imshow("img2", img2)
cv2.waitKey(0)