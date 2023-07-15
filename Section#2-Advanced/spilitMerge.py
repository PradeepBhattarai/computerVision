import cv2 as cv
import numpy as np

img=cv.imread('./Resources/Photos/park.jpg')
# cv.imshow('Boston',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
# cv.imshow('Blank',blank)

b,g,r=cv.split(img)

# cv.imshow('Green',g)
# cv.imshow('Blue',b)
# cv.imshow('Red',r)

merged=cv.merge([b,g,r])
# cv.imshow('Merged',merged)


blue=cv.merge([b,blank,blank])
cv.imshow('blue',blue)

green=cv.merge([blank,g,blank])
cv.imshow('green',green)

red=cv.merge([blank,blank,r])
cv.imshow('RED',red)


cv.waitKey(0)