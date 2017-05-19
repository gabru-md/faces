# PYTHON
# MANISH DEVGAN
# https://github.com/gabru-md

#BEGIN

# a very simple OpenCV program


import cv2

imagePath = "PATH TO THE IMAGE YOU WANT TO OPEN"

_im = cv2.imread(imagePath) # reading the image

# now to show the image

cv2.imshow("JUST TYPE IN WHATEVER YOU WANT TO NAME IT!", _im)

cv2.waitKey(0)


#END
