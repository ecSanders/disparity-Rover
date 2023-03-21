"""
Title: depth_frame.py
Authors: Jared Perlic
Date Start: Mar 22, 2023
Description:

This script generates a depth map from a stereo image.
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
M = cv_file.getNode("M").real()
cv_file.release()

# Create the StereoBM object
stereo = cv.StereoBM_create(numDisparities=numDisparities, blockSize=blockSize)

# Calculate disparity using the StereoBM algorithm
disparity = stereo.compute(imgL, imgR)

# Display the disparity map
plt.imshow(disparity, "gray")
plt.show()

# Calculate inverse disparity
# ||    depth = M * (1 / disparity)    ||
value_pairs = np.array([])
z = value_pairs[:,0]
disp = value_pairs[:,1]
disp_inv = 1 / disp

# Plot the relation depth and corresponding disparity
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.plot(disp, z, 'o-')
ax1.set(xlabel='Normalized disparity value', ylabel='Depth from camera (cm)',
       title='Relation between depth \n and corresponding disparity')
ax1.grid()
ax2.plot(disp_inv, z, 'o-')
ax2.set(xlabel='Inverse disparity value (1/disp)', ylabel='Depth from camera (cm)',
       title='Relation between depth \n and corresponding inverse disparity')
ax2.grid()
plt.show()

# Solve for M using least square fitting with QR decomposition method
coeff = np.vstack([disp_inv, np.ones(len(disp_inv))]).T
ret, sol = cv.solve(coeff, z, flags=cv.DECOMP_QR)
M = sol[0,0]
C = sol[1,0]
print("Value of M = ", M)