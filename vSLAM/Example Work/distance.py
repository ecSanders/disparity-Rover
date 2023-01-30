'''
Title: distance.py
Authors: Jared Perlic
Date Start: Jan 30, 2023
Description:

This script find the distance between the camera and the feature in an image.
'''

import cv2 as cv
import numpy as np
import imutils
from imutils import paths

# Initialize the known distance from the camera to the marker
DISTANCE = 24

# Initialize the marker's known width
WIDTH = 11

def distance_to_camera(kw, fl, pw):
    """Computes and returns the distance from the marker to the camera.
    
    param kw: The known width of the marker
    param fl: The computed focal length
    param pw: The perceived width of an object in pixels"""

    return (kw * fl) / pw

def find_marker(img):
    """Finds a marker (object) to compute the distance to."""

    # Convert to grayscale, then blur and detect edges
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (5, 5), 0)
    edged = cv.Canny(gray, 35, 125)

    # Find the contours in the edged image and keep the largest
    cnts = cv.findContours(edged.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv.contourArea)

	# Compute and return the bounding box of the of the marked region
    return cv.minAreaRect(c)

img = cv.imread('../../Images/stitch01_med.jpg')
marker = find_marker(img)
fl = (marker[1][0] * DISTANCE) / WIDTH

for imgPath in sorted(paths.list_images('../../Images')):

    # Load the image and find the marker
	img = cv.imread(imgPath)
	marker = find_marker(img)

    # Compute the distance from the camera to the marker
	inches = distance_to_camera(WIDTH, fl, marker[1][0])

	# Draw and display a bounding box around the image
	box = cv.cv.BoxPoints(marker) if imutils.is_cv2() else cv.boxPoints(marker)
	box = np.int0(box)
	cv.drawContours(img, [box], -1, (0, 255, 0), 2)

    # Display text
	cv.putText(img, "%.2fft" % (inches / 12),
		(img.shape[1] - 200, img.shape[0] - 20),
        cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)

	cv.imshow('Distance to Camera', img)
	cv.waitKey(0)