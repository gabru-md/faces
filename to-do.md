### This is the TO-DO File

###### Update this File if any new idea pops up!
###### Or if the process to do the work is developed and only waiting to be coded right!

### Content Initialised : 20 May 2017

Check for Faces in Images !<br>
Check for Faces in Images where Face is not straight, i.e., Face is tilted leftwards or rightwards.

### Updates
#### Dates
 * 20 May 2017
 * 21 May 2017
### How To Implement

#### Check for Faces in Images where Face is not straight, i.e., Face is tilted leftwards or rightwards:
  * Open an Image and Try to Detect the tilted Face at first! <--- Done
  * It was just a try! <--- Done
  * Follow the steps below until the Face gets Accurately Detected! <--- Done
  * Rotate the Image Matrix through a certain 'theta'. <--- Done
  * Use cv2.getRotationMatrix2d() to rotate the matrix and store the output matrix in 'M'! <--- Done
  * Rotate the Image using the 'M' Matrix. <--- Done till here
  * Check for EYES instead of Face!
  * It is because EYES can be used as a measure of straightness of face in the particular rotation of image!
  * Now create boxes / rectangle around the Eyes.
  * Create box / rectangle around the face as well.
  * Get the dimensions of Eyes from OpenCV.
  * Check if the level of both Eyes are same!
      * Checking this will ensure the straightness of face.
      * If the Eyes are on same LEVEL then we can "ASSUME" that our Face is Straight!
  * Stop Rotating if the image LEVEL is same.
  * We can now "ASSUME" that the Face is Detected accurately
  


### Author
#### [Manish Devgan](https://github.com/gabru-md)
