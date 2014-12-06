
#coding=utf-8
import cv2
import numpy as np

img = cv2.imread("20.jpg", 0)  #Canny只能处理灰度图，所以将读取的图像转成灰度图

img = cv2.GaussianBlur(img,(3,3),0) #高斯平滑处理原图像降噪
canny = cv2.Canny(img, 50, 150)     #apertureSize默认为3

cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()




def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray,(3,3),0)
    detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('canny demo',dst)

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3

img = cv2.imread('20.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('canny demo')

cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)

CannyThreshold(0)  # initialization
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()