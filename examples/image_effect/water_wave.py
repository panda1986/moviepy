#水波纹效果
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

# Define water wave effects parameters 
wavelength = 20
amplitude = 30
phase = math.pi / 4

# Get the center point 
centreX = 0.5
centreY = 0.5
radius = min(rows, cols) / 2

# Set the water wave coverage 
icentreX = cols*centreX
icentreY = rows*centreY

# Image water wave effects 
for i in range(rows):
    for j in range(cols):
        dx = j - icentreX
        dy = i - icentreY
        distance = dx*dx + dy*dy
        if distance>radius*radius:
            x = j
            y = i
        else:
            # Calculate the water wave region 
            distance = math.sqrt(distance)
            amount = amplitude * math.sin(distance / wavelength * 2*math.pi - phase)
            amount = amount * (radius-distance) / radius
            amount = amount * wavelength / (distance+0.0001)
            x = j + dx * amount
            y = i + dy * amount

        # Boundary judgment 
        if x<0:
            x = 0
        if x>=cols-1:
            x = cols - 2
        if y<0:
            y = 0
        if y>=rows-1:
            y = rows - 2
        p = x - int(x)
        q = y - int(y)

        # Image water wave assignment 
        dst[i, j, :] = (1-p)*(1-q)*img[int(y),int(x),:] + p*(1-q)*img[int(y),int(x),:]
        + (1-p)*q*img[int(y),int(x),:] + p*q*img[int(y),int(x),:]

# Display images 
cv2.imshow('src', img)
cv2.imshow('dst', dst)
# Wait for the display 
while (1):
    if cv2.waitKey(100) == 27:
        break
cv2.destroyAllWindows()