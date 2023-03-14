"""
Title: disparity_frame.py
Authors: Jared Perlic
Date Start: Mar 15, 2023
Description:

This script generates a disparity map from a stereo image.
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

imgL = cv.imread('../../Images/stitch01_med.jpg', cv.IMREAD_GRAYSCALE)
imgR = cv.imread('../../Images/stitch02_med.jpg', cv.IMREAD_GRAYSCALE)

# Reading the stored StereoBM parameters
cv_file = cv.FileStorage("disparity_params.xml", cv.FILE_STORAGE_READ)
numDisparities = int(cv_file.getNode("numDisparities").real())
blockSize = int(cv_file.getNode("blockSize").real())
preFilterType = int(cv_file.getNode("preFilterType").real())
preFilterSize = int(cv_file.getNode("preFilterSize").real())
preFilterCap = int(cv_file.getNode("preFilterCap").real())
textureThreshold = int(cv_file.getNode("textureThreshold").real())
uniquenessRatio = int(cv_file.getNode("uniquenessRatio").real())
speckleRange = int(cv_file.getNode("speckleRange").real())
speckleWindowSize = int(cv_file.getNode("speckleWindowSize").real())
disp12MaxDiff = int(cv_file.getNode("disp12MaxDiff").real())
minDisparity = int(cv_file.getNode("minDisparity").real())
cv_file.release()

# Create the StereoBM object
stereo = cv.StereoBM_create(numDisparities=numDisparities, blockSize=blockSize)

# Calculate disparity using the StereoBM algorithm
disparity = stereo.compute(imgL, imgR)

# Display the disparity map
plt.imshow(disparity, "gray")
plt.show()