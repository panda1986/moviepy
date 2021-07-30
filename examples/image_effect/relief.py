# -*- coding: utf-8 -*-
#By:Eastmount CSDN 2020-12-22
import cv2
import numpy as np

# Read the original image 
img = cv2.imread('../sources/xafanda.png', 1)

# Get the height and width of the image 
height, width = img.shape[:2]

# Image gray processing 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Create target image 
dstImg = np.zeros((height,width,1),np.uint8)

# Relief effect algorithm ：newPixel = grayCurrentPixel - grayNextPixel + 150
for i in range(0,height):
    for j in range(0,width-1):
        grayCurrentPixel = int(gray[i,j])
        grayNextPixel = int(gray[i,j+1])
        newPixel = grayCurrentPixel - grayNextPixel + 150
        if newPixel > 255:
            newPixel = 255
        if newPixel < 0:
            newPixel = 0
        dstImg[i,j] = newPixel

# Display images 
cv2.imshow('src', img)
cv2.imshow('dst',dstImg)

# Wait for the display 
while (1):
    if cv2.waitKey(100) == 27:
        break

cv2.destroyAllWindows()