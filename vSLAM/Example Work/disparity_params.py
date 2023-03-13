"""
Title: disparity_params.py
Authors: Jared Perlic
Date Start: Mar 13, 2023
Description:

This script allows the user to find optimal parameters for the disparity maps.
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

def nothing(x):
    pass

cv.namedWindow("disp", cv.WINDOW_NORMAL)
cv.resizeWindow("disp", 600, 600)
 
cv.createTrackbar("numDisparities", "disp", 1, 17, nothing)
cv.createTrackbar("blockSize", "disp", 5, 50, nothing)
cv.createTrackbar("preFilterSize", "disp", 2, 25, nothing)
cv.createTrackbar("preFilterCap", "disp", 5, 62, nothing)
cv.createTrackbar("textureThreshold", "disp", 10, 100, nothing)
cv.createTrackbar("uniquenessRatio", "disp", 15, 100, nothing)
cv.createTrackbar("speckleRange", "disp", 0, 100, nothing)
cv.createTrackbar("speckleWindowSize", "disp", 3, 25, nothing)
cv.createTrackbar("disp12MaxDiff", "disp", 5, 25, nothing)
cv.createTrackbar("minDisparity", "disp", 5, 25, nothing)
 
# Create an object of StereoBM algorithm
stereo = cv.StereoBM_create()

while True:

    # Capture and store left and right camera images
    retL, imgL = CamL.read()
    retR, imgR = CamR.read()

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

        # Update the parameters based on the trackbar positions
        numDisparities = cv.getTrackbarPos("numDisparities", "disp") * 16
        blockSize = cv.getTrackbarPos("blockSize", "disp") * 2 + 5
        preFilterSize = cv.getTrackbarPos("preFilterSize", "disp") * 2 + 5
        preFilterCap = cv.getTrackbarPos("preFilterCap", "disp")
        textureThreshold = cv.getTrackbarPos("textureThreshold", "disp")
        uniquenessRatio = cv.getTrackbarPos("uniquenessRatio", "disp")
        speckleRange = cv.getTrackbarPos("speckleRange", "disp")
        speckleWindowSize = cv.getTrackbarPos("speckleWindowSize", "disp") * 2
        disp12MaxDiff = cv.getTrackbarPos("disp12MaxDiff", "disp")
        minDisparity = cv.getTrackbarPos("minDisparity", "disp")
        
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


print("Saving disparity parameters...")

cv_file = cv.FileStorage("disparity_params.xml", cv.FILE_STORAGE_WRITE)
cv_file.write("numDisparities", numDisparities)
cv_file.write("blockSize", blockSize)
cv_file.write("preFilterType", 1)
cv_file.write("preFilterSize", preFilterSize)
cv_file.write("preFilterCap", preFilterCap)
cv_file.write("textureThreshold", textureThreshold)
cv_file.write("uniquenessRatio", uniquenessRatio)
cv_file.write("speckleRange", speckleRange)
cv_file.write("speckleWindowSize", speckleWindowSize)
cv_file.write("disp12MaxDiff", disp12MaxDiff)
cv_file.write("minDisparity", minDisparity)
cv_file.release()