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
    print '正在处理中',
    img = cv2.imread(fn)
    w=img.shape[1]
    h=img.shape[0]
    ii=0
    #关于纵向生成镜像
    #
    mirror_w=w/2
    for j in xrange(0,h):
        for i in xrange(0,mirror_w):
            img[j,i,:]=img[j,w-i-1,:]
        print '.',
    #加上水印
    cv2.putText(img,"http://blog.csdn.net/myhaspl", (20,20),cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 0), thickness = 2)
    cv2.putText(img,"code by myhaspl:myhaspl@qq.com", (20,100),cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 0), thickness = 2)
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()