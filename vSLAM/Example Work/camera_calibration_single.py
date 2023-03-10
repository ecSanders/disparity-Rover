'''
Title: camera_calibration_single.py
Authors: Erik Sanders
Date Start: Jan 30, 2023

Description: 

This script calibrates our camera and returns RMSE, camera matrix, distortion coefficients, 
per frame rotations and translations. Of importance is the RMSE value. This gives the per 
pixel projection error. Anything under 1 is very good. You might be able to get away with up to 2 or 3.
'''
import cv2
import numpy as np
import glob

def calibrate_camera(images_folder):
    images_names = sorted(glob.glob(images_folder))
    images = []
    for imname in images_names:
        im = cv2.imread(imname, 1)
        images.append(im)
 
    #criteria used by checkerboard pattern detector.
    #Change this if the code can't find the checkerboard
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
 
    rows = 4 #number of checkerboard rows.
    columns = 5 #number of checkerboard columns.
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
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        


        # cv2.imshow("yeello", res)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        #find the checkerboard
        ret, corners = cv2.findChessboardCorners(gray, (rows, columns), None)

        # False
        print(ret)

        if ret == True:
 
            #Convolution size used to improve corner detection. Don't make this too large.
            conv_size = (11, 11)
 
            #opencv2 can attempt to improve the checkerboard coordinates
            corners = cv2.cornerSubPix(gray, corners, conv_size, (-1, -1), criteria)
            cv2.drawChessboardCorners(frame, (rows,columns), corners, ret)
            cv2.imshow('img', frame)
            k = cv2.waitKey(500)
 
            objpoints.append(objp)
            imgpoints.append(corners)
 
 
    # ERROR 1,2
    # print(objpoints, imgpoints, width, height)
    print(objpoints, imgpoints, width, height)
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, (width, height), None, None)
    print('rmse:', ret)
    print('camera matrix:\n', mtx)
    print('distortion coeffs:', dist)
    print('Rs:\n', rvecs)
    print('Ts:\n', tvecs)
 
    return mtx, dist
 
mtx1, dist1 = calibrate_camera(images_folder = '../../Images/calibration/D2/*')
mtx2, dist2 = calibrate_camera(images_folder = '../../Images/calibration/J2/*')
