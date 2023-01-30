'''
Title: capture2.py
Authors: Jared Perlic, Erik Sanders
Date Start: Jan 30, 2023
Description:

This script runs a webcam and displays the feed live. It 
also feature matches between the two images as well
'''
import cv2 as cv

# Initiate ORB detector
orb = cv.ORB_create()

# Create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# Define two VideoCapture objects
camL = cv.VideoCapture(1)  # Camera ID for left camera
camR = cv.VideoCapture(2)  # Camera ID for right camera

while True:

    # Capture video frame by frame
    retL, frameL = camL.read()
    retR, frameR = camR.read()

    # Run feature detection
    kp1, des1 = orb.detectAndCompute(frameL, None)
    kp2, des2 = orb.detectAndCompute(frameR, None)

    # Match descriptors
    matches = bf.match(des1, des2)


    # Sort them in the order of their distance
    matches = sorted(matches, key=lambda x:x.distance)

    # Draw first 15 matches
    img3 = cv.drawMatches(frameL, kp1, frameR, kp2, matches[:15], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Display the video
    cv.imshow('Joined Features', img3)
    # cv.imshow('dispR', frameR)
    
    # Press `q` to close the window
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture objects
camL.release()
camR.release()

cv.destroyAllWindows()