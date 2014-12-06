#coding=utf-8

import cv2
import numpy as np

img = cv2.imread("6.jpg")
b,g,r = cv2.split(img)
cv2.imshow("Blue",r)
cv2.imshow("Red",g)
cv2.imshow("Green",b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 也可以单独返回其中一个通道
b = cv2.split(img)[0]  # B通道
g = cv2.split(img)[1]  # G通道
r = cv2.split(img)[2]  # R通道




#使用Numpy 数组来实现图像通道分离
img = cv2.imread("7.jpg")
# 创建3个跟图像一样大小的矩阵，数值全部为0
b = np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
g = np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
r = np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)

#复制图像通道里的数据
b[:,:] = img[:,:,0]  # 复制 b 通道的数据
g[:,:] = img[:,:,1]  # 复制 g 通道的数据
r[:,:] = img[:,:,2]  # 复制 r 通道的数据

cv2.imshow("Blue",b)
cv2.imshow("Red",r)
cv2.imshow("Green",g)
cv2.waitKey(0)
cv2.destroyAllWindows()


img = cv2.imread("ur.jpg")

b = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
g = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
r = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)

b[:,:] = img[:,:,0]
g[:,:] = img[:,:,1]
r[:,:] = img[:,:,2]

merged = cv2.merge([b,g,r])
print "Merge by OpenCV"
print merged.strides
print merged

mergedByNp = np.dstack([b,g,r])
print "Merge by NumPy "
print mergedByNp.strides
print mergedByNp

cv2.imshow("Merged", merged)
cv2.imshow("MergedByNp", mergedByNp)
cv2.imshow("Blue", b)
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.waitKey(0)
cv2.destroyAllWindows()