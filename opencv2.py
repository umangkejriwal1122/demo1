
#### Open Webcam  #####

import cv2
cap=cv2.VideoCapture(0)   ## if multiple webcams are there...0 is first camera

##  cap.read() returns two variable ret(return) and frame(numpy.ndarray)
## while because is video is a series of images 
while True:
    ret,frame=cap.read()
    print(ret)
    print(frame)
 #   img1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('WebCam',frame)
 #   cv2.imshow('WebCam',img1)
    if cv2.waitKey(1)==13:    ## 13 ASCII Code of Enter...when enter pressed it releases
        break
     
cap.release()
cv2.destroyAllWindows()





#### Image Capture Using Webcam  #####

import cv2
import matplotlib.pyplot as plt
cap=cv2.VideoCapture(0)   ## if multiple webcams are there...0 is first camera

if cap.isOpened():
    ret,frame=cap.read()
    print(ret)
    print(frame)
else:
    ret=False
    
# converts captured image form BGR to RGB   
img1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.title("My Image")
plt.xticks([])    ## hides x axis values
plt.yticks([])    ## hides y axis values
plt.show()
cap.release()




#### Webcam Resolution  #####

import cv2
cap=cv2.VideoCapture(0)  

print('Width :'+str(cap.get(3)))     ## 3 for width
print('Height :'+str(cap.get(4)))     ## 3 for width

cap.set(3,1200)
cap.set(4,900)

print('Width :'+str(cap.get(3)))     ## 3 for width    adjust to maxm possible resolution
print('Height :'+str(cap.get(4)))     ## 3 for width

while True:
    ret,frame=cap.read()
    cv2.imshow('WebCam',frame)
    if cv2.waitKey(1)==13:
        break
     
cap.release()
cv2.destroyAllWindows()


#### Video Capture and Save to disk  #####

import cv2

cv2.namedWindow("Live Video Capture")
cap=cv2.VideoCapture(0)

filename=r'C:\Users\umang\Desktop\CV\Output\Video.avi'  ## path to save

## coding and encoding, fourcc - four character code
## Popular formats -- WMV2, WMV1, MJPG, DIVX, XVID, H264 ---- XVID gerally used on internet for streaming

codec = cv2.VideoWriter_fourcc('X','V','I','D')
framerate=30     ## for persistence of vision minm 24 25 is reqd... 30 is pretty smooth
resolution=(640,480)

VideoFileOutput = cv2.VideoWriter(filename,codec,framerate,resolution)  ## creates a file in memory

while ret:
    ret,frame=cap.read()
  ##  frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
  ##  frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)   # hue saturation value
    VideoFileOutput.write(frame)
    cv2.imshow('Video',frame)
  
    if cv2.waitKey(1)==13:    ## 13 ASCII Code of Enter...when enter pressed it releases
        break
 
cv2.destroyAllWindows()    
VideoFileOutput.release()
cap.release()





  

