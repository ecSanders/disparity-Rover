'''
Title: capture1.py
Authors: Jared Perlic
Date Start: Jan 30, 2023
Description:

This script runs a webcam and displays the feed live.
'''

import cv2 as cv
import numpy as np
import glob
import pickle

# Define a VideoCapture object
cam = cv.VideoCapture(1)
i=0
rows=5
columns=6
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
world_scaling = 1. #change this to the real world square size. Or not.

#coordinates of squares in the checkerboard world space
objp = np.zeros((rows*columns,3), np.float32)
objp[:,:2] = np.mgrid[0:rows,0:columns].T.reshape(-1,2)
objp = world_scaling* objp



#Pixel coordinates of checkerboards
imgpoints = [] # 2d points in image plane.

#coordinates of the checkerboard in checkerboard world space.
objpoints = [] # 3d point in real world space

while True:

    # Capture video frame by frame
    ret, frame = cam.read()


    #frame dimensions. Frames should be the same size.
    width = frame.shape[1]
    height = frame.shape[0]

    cv.imshow("yeello", frame)
    

    #find the checkerboard
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, (rows, columns), None)

    if ret == True:
        #Convolution size used to improve corner detection. Don't make this too large.
        conv_size = (11, 11)

        #opencv2 can attempt to improve the checkerboard coordinates
        corners = cv.cornerSubPix(gray, corners, conv_size, (-1, -1), criteria)
        cv.drawChessboardCorners(frame, (rows,columns), corners, ret)
        cv.imshow('img', frame)
        cv.waitKey(0)

        objpoints.append(objp)
        imgpoints.append(corners)


        # ERROR 1,2
        # print(objpoints, imgpoints, width, height)
        print(objpoints, imgpoints, width, height)
        ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, (width, height), None, None)
        print('rmse:', ret)
        print('camera matrix:\n', mtx)
        print('distortion coeffs:', dist)
        print('Rs:\n', rvecs)
        print('Ts:\n', tvecs)

        output = {"objpoints":objpoints, 
                  "imgpoints":imgpoints,
                  "camMat":mtx,
                  "Dist coeffs":dist}
        with open("calibrate02.pkl", 'wb') as f:  # open a text file
            pickle.dump(output, f) # serialize the list

    # Press `q` to close the window
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cam.release()

cv.destroyAllWindows()