#-*- coding: utf-8 -*-
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
    #生成日落效果
    #b[:,:] = img[:,:,0]
    #g[:,:] = img[:,:,1]
    #r[:,:] = img[:,:,2]
    for xi in xrange(0,w):
        for xj in xrange (0,h):
            img[xj,xi,0]= int(img[xj,xi,0]*0.7)
            img[xj,xi,1]= int(img[xj,xi,1]*0.7)
        if  xi%10==0 :print '.',
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()