# -*- coding: utf-8 -*-
#By:Eastmount CSDN 2020-12-22
import cv2
import numpy as np
# Read the original image 
src = cv2.imread('../sources/audrey2.png')
# Image gray processing 
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# Custom convolution kernel 
kernel = np.array([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]])
#kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
# Image relief effect 
output = cv2.filter2D(gray, -1, kernel)
# Display images 
cv2.imshow('Original Image', src)
cv2.imshow('Emboss_1',output)

# Wait for the display 
while (1):
    if cv2.waitKey(100) == 27:
        break
    
cv2.destroyAllWindows()