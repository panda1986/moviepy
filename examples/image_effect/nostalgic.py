#coding:utf-8
#By:Eastmount CSDN 2020-12-22
import cv2
import numpy as np

# Read the original image 
img = cv2.imread('../sources/audrey2.png')

# Get image rows and columns 
rows, cols = img.shape[:2]

# New target image 
dst = np.zeros((rows, cols, 3), dtype="uint8")

# Image nostalgic effects 
for i in range(rows):
    for j in range(cols):
        B = 0.272*img[i,j][2] + 0.534*img[i,j][1] + 0.131*img[i,j][0]
        G = 0.349*img[i,j][2] + 0.686*img[i,j][1] + 0.168*img[i,j][0]
        R = 0.393*img[i,j][2] + 0.769*img[i,j][1] + 0.189*img[i,j][0]
        if B>255:
            B = 255
        if G>255:
            G = 255
        if R>255:
            R = 255
        dst[i,j] = np.uint8((B, G, R))

# Display images 
cv2.imshow('src', img)
cv2.imshow('dst', dst)
# Wait for the display 
while (1):
    if cv2.waitKey(100) == 27:
        break
cv2.destroyAllWindows()

# 显示速度较慢， 处理速度太慢？