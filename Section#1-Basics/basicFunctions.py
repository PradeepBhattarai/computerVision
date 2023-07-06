import cv2 as cv

img=cv.imread('../Resources/Photos/cat.jpg')
#Original image show
cv.imshow('Cat',img)

# Converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# Blur image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

#Edge Cascade
# edge detection in real image
cany=cv.Canny(img,125,175)
# cv.imshow('Canny Edges',cany)

# Edge detection in blured image
cany1=cv.Canny(blur,125,175)
# cv.imshow('Canny Edges1',cany1)

# Dilating the image 
dilated=cv.dilate(cany,(3,3),iterations=1)
# cv.imshow('Dilated',dilated)

#Eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
# cv.imshow('Eroded',eroded)

#Resize
resized=cv.resize(img,(1000,800),interpolation=cv.INTER_CUBIC)
# for shrinking we use cv.INTER_AREA and for enlarging cv.INTER_LINEAR or cv.INTER_CUBIC which improves quality

# cv.imshow('Resized',resized)

# Croping 
cropped=img[50:200,200:500]
cv.imshow('Cropped',cropped)


cv.waitKey(0)