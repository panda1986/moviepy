#流年效果
#coding:utf-8
#By:Eastmount CSDN 2020-12-22
import cv2
import math
import numpy as np

# Read the original image 
img = cv2.imread('../sources/audrey2.png')

# Get image rows and columns 
rows, cols = img.shape[:2]

# New target image 
dst = np.zeros((rows, cols, 3), dtype="uint8")

# Image fleeting effects 
for i in range(rows):
    for j in range(cols):
        #B The square root of the channel is multiplied by the parameter 12
        B = math.sqrt(img[i,j][0]) * 12
        G = img[i,j][1]
        R = img[i,j][2]
        if B>255:
            B = 255
        dst[i,j] = np.uint8((B, G, R))

# Display images 
cv2.imshow('src', img)
cv2.imshow('dst', dst)

# Wait for the display 
while (1):
    if cv2.waitKey(100) == 27:
        break

cv2.destroyAllWindows()