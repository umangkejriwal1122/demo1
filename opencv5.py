##### Object Tracking By Color #####

import cv2
import numpy as np

def main():
    windowName = "Preview"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
    
        ret, frame = cap.read()
        ## BGR/RGB is not good for color detection...HSV will be fine
        ## converting the frame to hsv that we are capturing
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Green Color (HSV value)
#        low = np.array([40, 50, 50])
 #       high = np.array([80, 255, 255])
        
        # Blue Color  
       # low = np.array([100, 50, 50])
       # high = np.array([140, 255, 255])
        
        # Red Color
        low = np.array([140, 150, 0])
        high = np.array([180, 255, 255])
        
        # image_mask returns a binary array of 0 and 1
        # Threshold the HSV image to get only blue/red/green colors
        image_mask = cv2.inRange(hsv, low, high)
        print (image_mask)
        
        #logical AND of mask and original image,ii will only show that colour
        output = cv2.bitwise_and(frame, frame, mask = image_mask)
        
        cv2.imshow("Original", frame)
        cv2.imshow("Mask", image_mask)
        cv2.imshow(windowName, output)
        if cv2.waitKey(1) == 27: # exit on ESC
            break

    cv2.destroyAllWindows()
    cap.release()
    
main()