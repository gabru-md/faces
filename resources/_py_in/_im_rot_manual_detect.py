# PYTHON
# MANISH DEVGAN
# https://github.com/gabru-md

# Program helps in detecting faces which are
# tilted right or left! The detection is done by 
# rotating the image and the trying to detect the 
# potential faces in it!

#BEGIN

# importing 

import cv2
import numpy as np
import os
import sys


# function to rotate the image to a specific angle begins
def rotate(img,angle):
    image = np.copy(img)
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

  # grab the rotation matrix (applying the negative of the
  # angle to rotate clockwise), then grab the sine and cosine
  # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

  # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

  # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

  # perform the actual rotation and return the image
    _im = cv2.warpAffine(image, M, (nW, nH))
  # a new vairable is taken instead of the old one as it will then form 2 different copies
  # instead of forming a reference of the object or altering the object itself

  # now show the rotated image!

    return _im
# function ends    

# reading image which is to be rotated
# this image will then be further looked in for faces at different angles
image = cv2.imread('te.jpg')

cascPath = "haarcascade_frontalface_default.xml"

os.chdir('C:\Users\Manish\Desktop')

# range is taken from 0 to 360 
# therefore we have range(360+1)

for i in range(361):
    # new object of image type or numpy.ndarray is created and named _im
    # this will have our rotated image
    _im = rotate(image,i)
    
    # converting our _im to grayscale to detect potential faces in it!
    _gray = cv2.cvtColor(_im,cv2.COLOR_BGR2GRAY)
    
    # declaring a classifier based on the cascade specified
    # in this case it is : 'haarcascade_frontalface_default.xml'
    faces = faceCascade.detectMultiScale(
    _gray,
    scaleFactor = 1.2,
    minNeighbors=1,
    minSize=(15,15),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    
    # drawing a box around the potential faces that have been identified
    
    for (x,y,w,h) in faces:
        cv2.rectangle(_im,(x+int(w*0.18),y+int(h*0.15)),(x+int(w*0.80),y+int(h*0.90)),(0,255,0),2)
        
    # showing the rotated image to the user!
    cv2.imshow('Rotated Image',_im)
    if cv2.waitKey(0) == 27:
        break

#END
