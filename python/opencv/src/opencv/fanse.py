import cv2.cv as cv
import cv2

image = cv.LoadImage('3.jpg',0)
size = (image.width,image.height)
iTmp = cv.CreateImage(size,image.depth,image.nChannels)
for i in range(image.height):
      for j in range(image.width):
          iTmp[i,j] = 255 - image[i,j]

cv.NamedWindow('image')
cv.NamedWindow('iTmp')
cv.ShowImage('image',image)
cv.ShowImage('iTmp',iTmp)
cv.WaitKey(0)