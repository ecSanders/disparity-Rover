'''
Title: capture2.py
Authors: Jared Perlic, Erik Sanders
Date Start: Jan 30, 2023
Description:

This script runs a webcam and displays the feed live.
'''
import cv2 as cv
import numpy as np


# Define two VideoCapture objects
cam = cv.VideoCapture(1)  # Camera ID for left camera

while True:

    # Capture video frame by frame
    retL, frame = cam.read()

    
    left = frame[0:960, 1280:2560]
    right = frame[0:960, 0:1280]

    print(left.shape, right.shape)
    joined = np.concatenate([left, right], axis=1)

    # resize
    sized = cv.resize(joined, (1280, 480))
    cv.imshow("Horizontal", sized)
    # Display the video
    

    # write images out as a stereo pair
    # cv.imwrite("../../Images/right.png", frameL)
    
    # Press `q` to close the window
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# Release the VideoCapture objects
cam.release()

cv.destroyAllWindows()