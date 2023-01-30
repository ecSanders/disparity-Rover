'''


Description: 

This script calibrates our camera and returns RMSE, camera matrix, distortion coefficients, 
per frame rotations and translations. Of importance is the RMSE value. This gives the per 
pixel projection error. Anything under 1 is very good. You might be able to get away with up to 2 or 3.
'''

import cv2 as cv
import numpy as np
import glob

images_folder = 'D2/*'
images_names = sorted(glob.glob(images_folder))
images = []
for imname in images_names:
    im = cv.imread(imname, 1)
    images.append(im)    


#criteria used by checkerboard pattern detector.
#Change this if the code can't find the checkerboard
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
 
rows = 5 #number of checkerboard rows.
columns = 8 #number of checkerboard columns.
world_scaling = 1. #change this to the real world square size. Or not.
 
#coordinates of squares in the checkerboard world space
objp = np.zeros((rows*columns,3), np.float32)
objp[:,:2] = np.mgrid[0:rows,0:columns].T.reshape(-1,2)
objp = world_scaling* objp
 
 
#frame dimensions. Frames should be the same size.
width = images[0].shape[1]
height = images[0].shape[0]
 
#Pixel coordinates of checkerboards
imgpoints = [] # 2d points in image plane.
 
#coordinates of the checkerboard in checkerboard world space.
objpoints = [] # 3d point in real world space
 
 
for frame in images:
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
    #find the checkerboard
    ret, corners = cv.findChessboardCorners(gray, (rows, columns), None)
 
    if ret == True:
 
        #Convolution size used to improve corner detection. Don't make this too large.
        conv_size = (11, 11)
 
        #opencv can attempt to improve the checkerboard coordinates
        corners = cv.cornerSubPix(gray, corners, conv_size, (-1, -1), criteria)
        cv.drawChessboardCorners(frame, (rows,columns), corners, ret)
        cv.imshow('img', frame)
        k = cv.waitKey(500)

objpoints.append(objp)
imgpoints.append(corners)