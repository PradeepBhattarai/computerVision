import cv2 as cv
import numpy as np

blank =np.zeros((500,500,3),dtype='uint8') #datatype of image
# cv.imshow('Blank',blank)

img=cv.imread('../Resources/Photos/cat.jpg')
# cv.imshow('Cat',img)

#1.Paing the image a certain colour
blank[200:300,300:400]=0,0,255
# cv.imshow('Green',blank)

#2.Draw the rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=-1)
# cv.imshow('Rectangle',blank)

# 3.Draw the circle 
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)

# 4.Draw the line
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
# cv.imshow('Line',blank)

# 5. Write Text on image
cv.putText(blank,'Hello',(2,200),cv.FONT_HERSHEY_TRIPLEX,5,(0,255,0),thickness=2)
cv.imshow('Text',blank)








cv.waitKey(0)