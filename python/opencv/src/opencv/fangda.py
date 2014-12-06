#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
import cv2
import numpy as np


fn="7.jpg"
if __name__ == '__main__':
    print 'http://blog.csdn.net/myhaspl'
    print 'myhaspl@qq.com'
    print
    print 'loading %s ...' % fn
    print 'working',
    img = cv2.imread(fn)
    w=img.shape[1]
    h=img.shape[0]
    sz1=w*2
    sz0=h*2
    #创建空白图像
    myimg1=np.zeros((sz0,sz1,3), np.uint8)
    #放大图像，每2个像素取1个像素的值
    temp_x=0
    temp_y=0
    for now_y in xrange(0,sz0):
        temp_x=0
        for now_x in xrange(0,sz1):
            myimg1[now_y,now_x,:]=img[int(temp_y),int(temp_x),:]
            temp_x+=0.5
            print '.',
        temp_y+=0.5


    cv2.namedWindow('img1')
    cv2.imshow('img1', myimg1)
    cv2.waitKey()
    cv2.destroyAllWindows()