import cv2 as cv
import numpy as np
from cvzone import stackImages
from cvzone.ColorModule import ColorFinder
from cvzone.FPS import FPS
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv.VideoCapture(
    r'C:\Users\abhin\Desktop\TrafficManagement\video\pexels-kelly-lacy-5473765.mp4')

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Display the resulting frame

        frame = cv.resize(frame, (960, 540))
        img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        img_canny = cv.Canny(img_gray, 100, 100)
        threshImg = cv.threshold(img_gray, 100, 200)

        frame = stackImages([frame, img_gray, img_canny], 2, 0.8)
        cv.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv.destroyAllWindows()
