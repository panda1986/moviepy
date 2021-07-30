#coding:utf-8
import cv2
import math
import numpy as np

# Get the filter color 
def getBGR(img, table, i, j):
    # Get the image color 
    b, g, r = img[i][j]
    # Calculate the position coordinates of colors in the standard color table 
    x = int(g/4 + int(b/32) * 64)
    y = int(r/4 + int((b%32) / 4) * 64)
    # Returns the corresponding color in the filter color table 
    return lj_map[x][y]

# Read the original image 
img = cv2.imread('../sources/xafanda.png')
lj_map = cv2.imread('../sources/audrey2.png')
# Get image rows and columns 
rows, cols = img.shape[:2]
# New target image 
dst = np.zeros((rows, cols, 3), dtype="uint8")
# Cycle through the filter colors 
for i in range(rows):
    for j in range(cols):
        dst[i][j] = getBGR(img, lj_map, i, j)
# Display images 
cv2.imshow('src', img)
cv2.imshow('dst', dst)
# Wait for the display 
while (1):
    if cv2.waitKey(100) == 27:
        break
cv2.destroyAllWindows()