# PYTHON
# MANISH DEVGAN
# https://github.com/gabru-md

#BEGIN

# To detect Faces in image!

import cv2
import os
import numpy as np
import sys

# change the directory to the one where you have the cascade downloaded

os.chdir("PATH TO THE DIRECTORY")

imagePath = "Path to image"

cascPath = "NAME OF THE FILE"

# Reading the image file to create a frame object named 'image'
image = cv2.imread(imagePath)

# converting it to grayscale to make our cascade detect faces

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# Declaring an object of CascadeClassifier type with our cascade 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

# getting the coordinates of faces!
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor = 1.2,
    minNeighbors=1,
    minSize=(15,15),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

# printing the total number of Faces in the Picture 
# the number of faces that the cascade has detected

print "Faces Detected: {0}".format(len(faces))

# creating rectangles around the faces that have been detected

for (x,y,w,h) in faces:
    #print faces 
    #print "\n"
    cv2.rectangle(image,(x+int(w*0.15),y+int(h*0.15)),(x+int(w*0.80),y+int(h*0.90)),(0,255,0),2)

# using cv2.imshow to show the image with detected faces on it!

cv2.imshow('FacesFound', image)
cv2.waitKey(0)

#END
