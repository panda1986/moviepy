# -*- coding: utf-8 -*-
#By:Eastmount CSDN 2020-12-22
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read the picture 
img = cv2.imread('../sources/audrey2.png')
source = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Gauss filtering 
result = cv2.GaussianBlur(source, (11,11), 0)
# Used to display Chinese labels normally 
plt.rcParams['font.sans-serif']=['SimHei']
# The graphics 
titles = [u' original image ', u' Gauss filtering ']
images = [source, result]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    plt.show()