#直方图均衡化
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
# Extract three color channels 
(b, g, r) = cv2.split(img)
# Color image equalization 
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
# Merge channel 
dst = cv2.merge((bH, gH, rH))
# Display images 
cv2.imshow('src', img)
cv2.imshow('dst', dst)

# Wait for the display 
while (1):
    if cv2.waitKey(100) == 27:
        break

cv2.destroyAllWindows()
