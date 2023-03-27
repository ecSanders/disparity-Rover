import cv2 as cv
import numpy as np

# Define VideoCapture object
Cam = cv.VideoCapture(1)

# Read and map values for stereo image rectification
cv_file = cv.FileStorage("data/params_py.xml", cv.FILE_STORAGE_READ)
Left_Stereo_Map_x = cv_file.getNode("Left_Stereo_Map_x").mat()
Left_Stereo_Map_y = cv_file.getNode("Left_Stereo_Map_y").mat()
Right_Stereo_Map_x = cv_file.getNode("Right_Stereo_Map_x").mat()
Right_Stereo_Map_y = cv_file.getNode("Right_Stereo_Map_y").mat()
cv_file.release()

# Define StereoBM parameters
minDisparity = 30
numDisparities = 160

# Create an object of StereoBM algorithm
stereo = cv.StereoBM_create(numDisparities=numDisparities, blockSize=15)

while True:

    # Capture and store left and right camera images
    ret, img = Cam.read()

    if ret:
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Split into left and right images
        imgL_gray = img_gray[0:960, 1280:2560]
        imgR_gray = img_gray[0:960, 0:1280]

        # Apply stereo image rectification on the left image
        Left_nice = cv.remap(imgL_gray,
                             Left_Stereo_Map_x,
                             Left_Stereo_Map_y,
                             cv.INTER_NEAREST)

        # Apply stereo image rectification on the right image
        Right_nice = cv.remap(imgR_gray,
                              Right_Stereo_Map_x,
                              Right_Stereo_Map_y,
                              cv.INTER_NEAREST)

        # Display rectified left and right
        cv.imshow("left", Left_nice)
        cv.imshow("right", Right_nice)

        # Calculate disparity using the StereoBM algorithm
        disparity = stereo.compute(Left_nice, Right_nice)
        # NOTE: Code returns a 16-bit signed single channel image,
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
        Cam = cv.VideoCapture(1)

# Release the VideoCapture objects
Cam.release()

cv.destroyAllWindows()