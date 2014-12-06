
# -*- coding: UTF-8 -*-
import cv2.cv as cv
import cv2
from cv2 import VideoCapture

cv.NamedWindow("W1", cv.CV_WINDOW_AUTOSIZE)


capture = cv.CaptureFromCAM(0)



def repeat():


        frame = cv.QueryFrame(capture)
        image_size = cv.GetSize(frame)

        greyscale = cv.CreateImage(image_size, 8, 1)
        cv.CvtColor(frame, greyscale, cv.CV_BGR2GRAY)
        storage = cv.CreateMemStorage(0)

        cv.EqualizeHist(greyscale, greyscale)


        # detect objects
        cascade = cv.Load('haarcascade_frontalface_alt.xml')


        faces = cv.HaarDetectObjects(greyscale, cascade, storage, 1.2, 2,
                                        cv.CV_HAAR_DO_CANNY_PRUNING,
                                        (50, 50))


        for (x,y,w,h) , n in faces:
            cv.Rectangle(frame, (x,y), (x+w,y+h), (0,0,255),20)
            cv.ShowImage("W1", greyscale)
        cv.ShowImage("W1", frame)


while True:
        repeat()
        c = cv.WaitKey(10)
        if c == 27:
            cv2.VideoCapture(0).release()
            cv2.destroyWindow("W1")
            break