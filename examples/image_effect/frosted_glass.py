# https://pythonmana.com/2020/12/20201224172431816U.html
#coding:utf-8
#By:Eastmount CSDN 2020-12-22
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the original image 
src = cv2.imread('../sources/xafanda.png')

# New target image 
dst = np.zeros_like(src)

# Get image rows and columns 
rows, cols = src.shape[:2]

# Define offsets and random numbers 
offsets = 5
random_num = 0

# Ground glass effect : The color of the random pixel in the neighborhood of the pixel replaces the color of the current pixel 
for y in range(rows - offsets):
    for x in range(cols - offsets):
        random_num = np.random.randint(0,offsets)
        dst[y,x] = src[y + random_num,x + random_num]

# Display images 
cv2.imshow('src',src)
cv2.imshow('dst',dst)

# Wait for the display 
while (1):
    if cv2.waitKey(100) == 27:
        break
    
cv2.destroyAllWindows()