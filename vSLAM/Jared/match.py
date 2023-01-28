import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

# Read images
img1 = cv.imread('../../Images/stitch01_med.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('../../Images/stitch02_med.jpg', cv.IMREAD_GRAYSCALE)

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

# Sort them in the order of their distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw first 10 matches
img3 = cv.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Stop the timer
stop = time.time()

# Print the time taken to match
print(f'Time to match: {round(stop - start, 2)}s')

plt.imshow(img3)
plt.show()