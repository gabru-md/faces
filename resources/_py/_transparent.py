# PYTHON
# MANISH DEVGAN
# https://github.com/gabru-md

# use OpenCV to add one image on another!

# Impose with transparency!
# same way like there is 'opacity' or 'rgba()' in CSS
#BEGIN

#IMPORTING MODULES

import cv2
import numpy as np

# reading images from the directory 
# using cv2.imread()

_im1 = cv2.imread("PATH TO IMAGE1")
_im2 = cv2.imread("PATH TO IMAGE2")

# now we will create a new numpy.ndarray object 
# for storing the image that will contain the imposed images!

_temp = cv2.addWeighted(_im1,0.5,_im2,0.5,0)

# the new variable is _temp
# cv2.addWeighted() is a function that can be used to impose one image on other

# cv2.addWeighted(IMAGE1,TRANSPARENCY(out of 1),IMAGE2,TRANSPARENCY(out of 1),GAMMA) <-- function def;

# show the image 

cv2.imshow('_temp',_temp)

cv2.waitKey(0)

#END
