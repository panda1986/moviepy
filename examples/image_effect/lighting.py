#coding:utf-8
#By:Eastmount CSDN 2020-12-22
import cv2
import math
import numpy as np

# Read the original image 
img = cv2.imread('../sources/audrey2.png')

# Get image rows and columns 
rows, cols = img.shape[:2]

# Set the center point 
centerX = rows / 2
centerY = cols / 2
print(centerX, centerY)
radius = min(centerX, centerY)
print(radius)

# Set light intensity 
strength = 200

# New target image 
dst = np.zeros((rows, cols, 3), dtype="uint8")

# Image lighting effects 
for i in range(rows):
    for j in range(cols):
        # Calculate the distance from the current point to the light Center ( The distance between two points in a plane coordinate system )
        distance = math.pow((centerY-j), 2) + math.pow((centerX-i), 2)
        # Get the original image 
        B = img[i,j][0]
        G = img[i,j][1]
        R = img[i,j][2]
        if (distance < radius * radius):
            # Calculate the enhanced illumination value according to the distance size 
            result = (int)(strength*( 1.0 - math.sqrt(distance) / radius ))
            B = img[i,j][0] + result
            G = img[i,j][1] + result
            R = img[i,j][2] + result
            # Judgement boundary To prevent cross-border 
            B = min(255, max(0, B))
            G = min(255, max(0, G))
            R = min(255, max(0, R))
            dst[i,j] = np.uint8((B, G, R))
        else:
            dst[i,j] = np.uint8((B, G, R))

# Display images 
cv2.imshow('src', img)
cv2.imshow('dst', dst)

# Wait for the display 
while (1):
    if cv2.waitKey(100) == 27:
        break
    
cv2.destroyAllWindows()