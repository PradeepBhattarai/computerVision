import cv2 as cv
import numpy as np


img=cv.imread('./Resources/Photos/cats 2.jpg')
cv.imshow('Cats',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
# cv.imshow('Blank Image',blank)

# mask=cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2+200,img.shape[0]//2+200),255,-1)
# cv.imshow('Mask',mask)

# masked=cv.bitwise_and(img,img,mask=mask)
# cv.imshow('Masked',masked)

circle=cv.circle(blank.copy(),(img.shape[1]//2+45,img.shape[0]//2),100,255,-1)
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

weired_shape=cv.bitwise_and(circle,rectangle)
# cv.imshow('Weired Shape',weired_shape)

masked=cv.bitwise_and(img,img,mask=weired_shape)
cv.imshow('Masked Weired_shaped',masked)


cv.waitKey(0)