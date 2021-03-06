# PYTHON
# MANISH DEVGAN
# https://github.com/gabru-md

#BEGIN

# ROTATE AN IMAGE IN PYTHON using OpenCV

# IMPORTS

import numpy as np
import cv2

# reading image using cv2.imread()

image = cv2.imread("PATH TO IMAGE")

# grab the dimensions of the image and then determine the
# center

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# grab the rotation matrix (applying the negative of the
# angle to rotate clockwise), then grab the sine and cosine
# (i.e., the rotation components of the matrix)
M = cv2.getRotationMatrix2D((cX, cY), -ve ANGLE, 1.0)
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

cv2.imshow('Rotated Image',_im)

#END
