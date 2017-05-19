# PYTHON
# MANISH DEVGAN
# https://github.com/gabru-md

# Simple program to open webcam and display your LIVE STREAM

#BEGIN

# Importing Modules
import numpy as np
import cv2

# creating the VideoCapture object to call our Camera

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # 'ret' is of type boolean
    # True means that frames are recorded and False means some error!
    
    # Display the resulting frame until the loop breaks!
    cv2.imshow('frame',frame)
    
    # press Esc key to exit out of the loop!
    if cv2.waitKey(1) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
# releasing is must else the samera wont stop recording the frames
cv2.destroyAllWindows()
