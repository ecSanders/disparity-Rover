"""
Title: disparity.py
Authors: Erik Sanders and Jared Perlic
Date Start: Mar 13, 2023
Description:

This script generates a disparity map from a stereo camera.
"""
import cv2 as cv
import numpy as np

CamL_id = 2  # Camera ID for left camera
CamR_id = 0  # Camera ID for right camera

# Define two VideoCapture objects
CamL = cv.VideoCapture(CamL_id)
CamR = cv.VideoCapture(CamR_id)

# Read and map values for stereo image rectification
cv_file = cv.FileStorage("stereo_rectify_maps.xml", cv.FILE_STORAGE_READ)
Left_Stereo_Map_x = cv_file.getNode("Left_Stereo_Map_x").mat()
Left_Stereo_Map_y = cv_file.getNode("Left_Stereo_Map_y").mat()
Right_Stereo_Map_x = cv_file.getNode("Right_Stereo_Map_x").mat()
Right_Stereo_Map_y = cv_file.getNode("Right_Stereo_Map_y").mat()
cv_file.release()
 
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
 
# Create an object of StereoBM algorithm
stereo = cv.StereoBM_create()

while True:

    # Capture and store left and right camera images
    retL, imgL = CamL.read()
    retR, imgR = CamR.read()

    # Display left and right camera images
    cv.imshow("left", imgL)
    cv.imshow("right", imgR)

    # Proceed only if the frames have been captured
    if retL and retR:
        imgR_gray = cv.cvtColor(imgR, cv.COLOR_BGR2GRAY)
        imgL_gray = cv.cvtColor(imgL, cv.COLOR_BGR2GRAY)

        # Apply stereo image rectification on the left image
        Left_nice = cv.remap(imgL_gray,
                             Left_Stereo_Map_x,
                             Left_Stereo_Map_y,
                             cv.INTER_LANCZOS4,
                             cv.BORDER_CONSTANT,
                             0)
        
        # Apply stereo image rectification on the right image
        Right_nice = cv.remap(imgR_gray,
                              Right_Stereo_Map_x,
                              Right_Stereo_Map_y,
                              cv.INTER_LANCZOS4,
                              cv.BORDER_CONSTANT,
                              0)
        
        # Set the updated parameters before computing disparity map
        stereo.setNumDisparities(numDisparities)
        stereo.setBlockSize(blockSize)
        stereo.setPreFilterSize(preFilterSize)
        stereo.setPreFilterCap(preFilterCap)
        stereo.setTextureThreshold(textureThreshold)
        stereo.setUniquenessRatio(uniquenessRatio)
        stereo.setSpeckleRange(speckleRange)
        stereo.setSpeckleWindowSize(speckleWindowSize)
        stereo.setDisp12MaxDiff(disp12MaxDiff)
        stereo.setMinDisparity(minDisparity)

        # Calculate disparity using the StereoBM algorithm
        disparity = stereo.compute(Left_nice, Right_nice)
        # NOTE: Code returns a 16bit signed single channel image,
        # CV_16S containing a disparity map scaled by 16. Hence it 
        # is essential to convert it to CV_32F and scale it down 16 times.
    
        # Convert to float32 
        disparity = disparity.astype(np.float32)
    
        # Scale down the disparity values and normalizing them 
        disparity = (disparity / 16.0 - minDisparity) / numDisparities
    
        # Display the disparity map
        cv.imshow("disp", disparity)

        # Press `q` to close the window
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    else:
        CamL = cv.VideoCapture(CamL_id)
        CamR = cv.VideoCapture(CamR_id)

# Release the VideoCapture objects
CamL.release()
CamR.release()

cv.destroyAllWindows()