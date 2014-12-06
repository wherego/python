#coding=utf-8

import cv2
import numpy as np

def salt(img, n):
    for k in range(n):
        #img.shape[0] -- 取得img 的列（图片的高）
        #img.shape[1] -- 取得img 的行（图片的宽）
        i = int(np.random.random() * img.shape[1]);
        j = int(np.random.random() * img.shape[0]);

        #判断是否为2维数组(即为灰度图像)
        if img.ndim == 2:
            img[j,i] = 255  #设置值为白点

        elif img.ndim == 3:   #判断是否为3维数组(即为RGB图像)
            img[j,i,0]= 255
            img[j,i,1]= 255
            img[j,i,2]= 255
    return img

if __name__ == '__main__':
    img = cv2.imread("x.jpg")
    saltImage = salt(img, 500)

    cv2.imshow("Salt", saltImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()