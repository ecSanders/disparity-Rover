'''
Title: depth.py
Authors: Jared Perlic
Date Start: Mar 8, 2023
Description:

This script generates a point cloud from a disparity map.
'''
import cv2 as cv
import numpy as np

camIdL = 2  # Camera ID for left camera
camIdR = 0  # Camera ID for right camera

# Define two VideoCapture objects
camL = cv.VideoCapture(camIdL)
camR = cv.VideoCapture(camIdR)

# Read and map values for stereo image rectification
cv_file = cv.FileStorage('stereo_rectify_maps.xml', cv.FILE_STORAGE_READ)
lStereoMapX = cv_file.getNode('Left_Stereo_Map_x').mat()
lStereoMapY = cv_file.getNode('Left_Stereo_Map_y').mat()
rStereoMapX = cv_file.getNode('Right_Stereo_Map_x').mat()
rStereoMapY = cv_file.getNode('Right_Stereo_Map_y').mat()
cv_file.release()
 
# Create an object of StereoBM algorithm
stereo = cv.StereoBM_create()

while True:

    # Capture and store left and right camera images
    retL, imgL = camL.read()
    retR, imgR = camR.read()

    # Proceed only if the frames have been captured
    if retL and retR:
        imgR_gray = cv.cvtColor(imgR, cv.COLOR_BGR2GRAY)
        imgL_gray = cv.cvtColor(imgL, cv.COLOR_BGR2GRAY)

        # Apply stereo image rectification on the left image
        Left_nice = cv.remap(imgL_gray,
                             lStereoMapX,
                             lStereoMapY,
                             cv.INTER_LANCZOS4,
                             cv.BORDER_CONSTANT,
                             0)
        
        # Apply stereo image rectification on the right image
        Right_nice = cv.remap(imgR_gray,
                              rStereoMapX,
                              rStereoMapY,
                              cv.INTER_LANCZOS4,
                              cv.BORDER_CONSTANT,
                              0)

        # Set the parameters
        numDisparities = 16
        blockSize = 15
        preFilterSize = 9
        preFilterCap = 5
        textureThreshold = 10
        uniquenessRatio = 15
        speckleRange = 0
        speckleWindowSize = 6
        disp12MaxDiff = 5
        minDisparity = 5
        
        # Set the parameters and compute disparity map
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
        # NOTE: Code returns a 16bit signed single channel image, CV_16S
        # containing a disparity map scaled by 16. Hence it is essential to
        # convert it to CV_32F and scale it down 16 times.
    
        # Convert to float32 
        disparity = disparity.astype(np.float32)
    
        # Scale down the disparity values and normalizing them 
        disparity = (disparity / 16.0 - minDisparity) / numDisparities
    
        # Display the disparity map
        cv.imshow('disp', disparity)

        h, w = imgL.shape[:2]
        f = w * 0.8
        Q = np.float32([[1, 0, 0, -0.5 * w],
                        [0, -1, 0, 0.5 * h],  # Turn points 180 degrees
                        [0, 0, 0, -f],        # So that y-axis looks up
                        [0, 0, 1, 0]])

        # Generate a point cloud and normalize
        img3D = cv.reprojectImageTo3D(disparity, Q)
        img3D_normalize = cv.normalize(img3D, None, 0, 1.0, cv.NORM_MINMAX, dtype=cv.CV_32F)

        # Press `q` to close the window
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        camL = cv.VideoCapture(camIdL)
        camR = cv.VideoCapture(camIdR)

# Release the VideoCapture objects
camL.release()
camR.release()

cv.destroyAllWindows()