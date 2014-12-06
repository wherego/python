# -*- coding: utf-8 -*-

##
# @brief 显示摄像头采样的图像，并接受键盘事件
# @author ShuaiLu
# @date 2014-06-09

import cv2

cv2.namedWindow('Video')

capture = cv2.VideoCapture(r'特种车识别.avi')
_, frame = capture.read()
while frame is not None:
    cv2.imshow('Video', frame)

    key = cv2.waitKey(10)
    if key == ord('s'):     # 当按下"s"键时，将保存当前画面
        cv2.imwrite('screenshot.bmp', frame)
    elif key == ord('q'):   # 当按下"q"键时，将退出循环
        break

    _, frame = capture.read()

cv2.destroyWindow('Video')