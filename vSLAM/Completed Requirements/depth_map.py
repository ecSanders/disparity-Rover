import numpy as np
import cv2
from matplotlib import pyplot as plt


# Define two VideoCapture objects
cam = cv2.VideoCapture(1)  # Camera ID for left camera

while True:

    # Capture video frame by frame
    retL, frame = cam.read()

    
    left = frame[0:960, 1280:2560]
    right = frame[0:960, 0:1280]


stereo = cv2.StereoSGBM_create(minDisparity=2,numDisparities=96, blockSize=19,\
                                preFilterCap=1, uniquenessRatio=3, speckleRange=3)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()


wsize=19
max_disp = 96
sigma = 1.5
lmbda = 8000.0
left_matcher = cv2.StereoBM_create(max_disp, wsize)
right_matcher = cv2.ximgproc.createRightMatcher(left_matcher)
left_disp = left_matcher.compute(imgL, imgR)
right_disp = right_matcher.compute(imgR, imgL)

# Now create DisparityWLSFilter
wls_filter = cv2.ximgproc.createDisparityWLSFilter(left_matcher)
# wls_filter.setLambda(lmbda)
# wls_filter.setSigmaColor(sigma)
filtered_disp = wls_filter.filter(left_disp, imgL, disparity_map_right=right_disp)

cv2.imshow("Filtered Img", filtered_disp)
cv2.waitKey(0)
cv2.destroyAllWindows()