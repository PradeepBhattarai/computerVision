import cv2 as cv

img=cv.imread('../Resources/Photos/cat_large.jpg')
#showing original image
cv.imshow('Cat',img)

#Function for resizing image
def rescaleFrame(frame,scale=0.25):
    #images, videos of file, for live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#Changing resolution of video
def changeRes(width,height):
    #Only works in live video
    capture.set(3,width)
    capture.set(4,height)


#resizing image
resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)



#Video Capture ->captures each frame
#for live video capture using camera we use 0 or 1 or ...
capture=cv.VideoCapture(0) 
#for capturing video from file we use file path '../Resources/Videos/dog.mp4'

while True:
    isTrue,frame=capture.read()

    frame_resized=rescaleFrame(frame)
    #original video
    cv.imshow('Video',frame)

    #Resized Video
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)