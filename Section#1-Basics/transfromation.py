import cv2 as cv
import numpy as np

img=cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Cat',img)

#Translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimesions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimesions)

#-ve x->Left
#-ve y ->Up
# +ve x -> right 
#+ve y ->Down

translated=translate(img,-100,-100)
# cv.imshow('Translated',translated)


#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2) #// returns integer
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,-45)
rottated=rotate(img,-90)
# cv.imshow('Rotated',rottated)

#Resizing image
resize=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
# cv.imshow('Resized',resize)

#Fliping image
flip=cv.flip(img,0) #0 for vertical 1 for horizongal and -1 for reverse mirror image flip

# cv.imshow('Flipped',flip)

#Cropping image
cropped=img[300:400,400:500]
cv.imshow('Cropped',cropped)



cv.waitKey(0) 

