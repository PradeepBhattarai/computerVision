import cv2 as cv

img=cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

# Averaging
average=cv.blur(img,(3,3))
cv.imshow('Average Blur',average)

#Gausing Blur
gausingBlur=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gausingBlur)

#Median Blur
medianBlur=cv.medianBlur(img,3)
cv.imshow('Median Blur',medianBlur)

#Bilateral Blur
bilateralBlur=cv.bilateralFilter(img,10,35,35)
cv.imshow('bilateralBlur',bilateralBlur)

cv.waitKey(0)