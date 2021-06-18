##### Image Thresholding #####
### Details in PDF Document ###

## Simple Thresholding ##

# If pixel value is greater than a threshold value, it is assigned one value (may be
# white), else it is assigned another value (may be black). The function used is 
# cv2.threshold. First argument is the source image, which should be a grayscale image. 
# Second argument is the threshold value which is used to classify the pixel values. 
# Third argument is the maxVal which represents the value to be given if pixel 
# value is more than (sometimes less than) the threshold value.

import cv2
import numpy as np
from matplotlib import pyplot as plt

# must be grayscale image
img = cv2.imread(r'C:\Users\umang\Desktop\CV\images\lena_color_512.tif',0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)   ## 127 = Global Value
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()



## Adaptive Thresholding  ##


# In the previous section, we used a global value as threshold value. But it 
# may not be good in all the conditions where image has different lighting conditions 
# in different areas. In that case, we go for adaptive thresholding. In this, the
# algorithm calculate the threshold for a small regions of the image. 
# So we get different thresholds for different regions of the same image and it 
# gives us better results for images with varying illumination.


# cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of 
# neighbourhood values where weights are a gaussian window


import cv2
from matplotlib import pyplot as plt
img = cv2.imread(r'C:\Users\umang\Desktop\CV\images\lena_color_512.tif',0)
img = cv2.medianBlur(img,5)    ## removes salt-and-pepper noise  (applied 50%)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)   ## ret return threshold value
print (ret)
# (src,maxValue,adaptiveMethod,thresholdType,blocksize,c)
# Block Size - It decides the size of neighbourhood area.
# C - It is just a constant which is subtracted from the mean or weighted 
# mean calculated.
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()







