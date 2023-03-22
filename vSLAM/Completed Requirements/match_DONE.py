'''
Title: match.py
Authors: Jared Perlic
Date Start: Jan 30, 2023
Description:

This script runs the feature matching.
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

# Read images
img1 = cv.imread('../../Images/left.png', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('../../Images/right.png', cv.IMREAD_GRAYSCALE)

# Initiate ORB detector
orb = cv.ORB_create()

# Find keypoints and descriptors
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# Start the timer
start = time.time()

# Match descriptors
matches = bf.match(des1, des2)

# Make sure at least 15 feature matches were found
assert len(matches) >= 15

# Sort them in the order of their distance
matches = sorted(matches, key=lambda x:x.distance)

# Draw first 10 matches
img3 = cv.drawMatches(img1, kp1, img2, kp2, matches[:15], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Stop the timer
stop = time.time()

# Print the time taken to match
print(f'Time to match: {round(stop - start, 2)}s')

plt.imshow(img3)
plt.show()