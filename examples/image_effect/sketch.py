#coding:utf-8
#By:Eastmount CSDN 2020-12-22
import cv2
import numpy as np
# Read the original image 
img = cv2.imread('../sources/audrey2.png')
# Image gray processing 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Gaussian filtering noise reduction 
gaussian = cv2.GaussianBlur(gray, (5,5), 0)
#Canny operator 
canny = cv2.Canny(gaussian, 50, 150)
# Threshold processing 
ret, result = cv2.threshold(canny, 100, 255, cv2.THRESH_BINARY_INV)
# Display images 
cv2.imshow('src', img)
cv2.imshow('result', result)

# Wait for the display 
while (1):
    if cv2.waitKey(100) == 27:
        break
cv2.destroyAllWindows()