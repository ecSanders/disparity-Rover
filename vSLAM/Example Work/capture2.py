'''
Title: capture2.py
Authors: Jared Perlic, Erik Sanders
Date Start: Jan 30, 2023
Description:

This script runs a webcam and displays the feed live.
'''
import cv2 as cv

# Define two VideoCapture objects
camL = cv.VideoCapture(1)  # Camera ID for left camera
camR = cv.VideoCapture(2)  # Camera ID for right camera

while True:

    # Capture video frame by frame
    retL, frameL = camL.read()
    retR, frameR = camR.read()

    # Display the video
    cv.imshow('dispL', frameL)
    cv.imshow('dispR', frameR)
    
    # write images out as a stereo pair
    cv.imwrite("../../Images/left.png", frameL)
    cv.imwrite("../../Images/right.png", frameR)
    
    # Press `q` to close the window
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# Release the VideoCapture objects
camL.release()
camR.release()

cv.destroyAllWindows()