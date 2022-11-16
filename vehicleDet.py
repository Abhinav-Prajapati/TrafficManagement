import cv2 as cv
import numpy as np

from cvzone import stackImages
# from cvzone.ColorModule import ColorFinder
# from cvzone.FPS import FPS

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv.VideoCapture(
    r'C:\Users\abhin\Desktop\TrafficManagement\video\pexels-kelly-lacy-5473765.mp4')

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

left_lane_count = 0
middle_lane_count = 0
right_lane_count = 0

old_1 = 1
old_2 = 1
old_3 = 1


def coutnCarLeft(pixalVal):
    global old_1
    global left_lane_count

    new = pixalVal

    if new == 200 and old_1 == 0:
        left_lane_count += 1
    old_1 = new


def coutnCarMiddle(pixalVal):
    global old_2
    global middle_lane_count

    new = pixalVal

    if new == 200 and old_2 == 0:
        middle_lane_count += 1
    old_2 = new


def coutnCarRight(pixalVal):
    global old_3
    global right_lane_count

    new = pixalVal

    if new == 200 and old_3 == 0:
        right_lane_count += 1
    old_3 = new


# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Display the resulting frame

        frame = cv.resize(frame, (960, 540))
        img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        img_canny = cv.Canny(img_gray, 100, 100)
        _, threshImg = cv.threshold(img_gray, 50, 200, cv.THRESH_BINARY)

        # Left lane
        cv.circle(frame, (267, 496), 5, (255, 0, 0), 5)
        # Middle lane
        cv.circle(frame, (475, 501), 5, (255, 0, 0), 5)
        # Right lane
        cv.circle(frame, (684, 498), 5, (255, 0, 0), 5)

        #print(f" Left {threshImg[496] [267]} Middle {threshImg[501][475]} Right {threshImg[498][684]} ")

        coutnCarLeft(threshImg[496][267])
        coutnCarMiddle(threshImg[501][475])
        coutnCarRight(threshImg[498][684])
        print(f"({left_lane_count},{middle_lane_count},{right_lane_count})")

        frame = stackImages([frame, img_gray, img_canny, threshImg], 2, 0.8)

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
