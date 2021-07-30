#卡通效果
#coding:utf-8
#By:Eastmount CSDN 2020-12-22
import cv2
import numpy as np
# Read the original image 
img = cv2.imread('../sources/audrey2.png')
# Define the number of bilateral filters 
num_bilateral = 7
# Use Gaussian pyramids to reduce sampling 
img_color = img
# Bilateral filtering 
for i in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)
    # Gray image conversion 
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Median filter processing 
    img_blur = cv2.medianBlur(img_gray, 7)
    # Edge detection and adaptive thresholding 
    img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)
    # Convert back to color image 
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    # And operation 
    img_cartoon = cv2.bitwise_and(img_color, img_edge)
# Display images 
cv2.imshow('src', img)
cv2.imshow('dst', img_cartoon)
# Wait for the display 
while (1):
    if cv2.waitKey(100) == 27:
        break
cv2.destroyAllWindows()