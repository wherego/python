#-*- coding: utf-8 -*-
import cv2
import numpy as np


fn="3.jpg"

if __name__ == '__main__':
    print 'http://blog.csdn.net/myhaspl'
    print 'myhaspl@qq.com'
    print
    print 'loading %s ...' % fn
    print '正在处理中',
    img = cv2.imread(fn)
    w=img.shape[1]
    h=img.shape[0]
    ii=0
    #生成底片
    b, g, r = cv2.split(img)
    b=255-b
    g=255-g
    r=255-r
    #直接通过索引改变色彩分量
    img[:,:,0]=b
    img[:,:,1]=g
    img[:,:,2]=r
    #加上水印
    cv2.putText(img,"http://blog.csdn.net/myhaspl", (20,20),cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 0), thickness = 2)
    cv2.putText(img,"code by myhaspl:myhaspl@qq.com", (20,100),cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 0), thickness = 2)
    cv2.namedWindow('img')
    cv2.imshow('img', img)

    cv2.waitKey()
    cv2.destroyAllWindows()