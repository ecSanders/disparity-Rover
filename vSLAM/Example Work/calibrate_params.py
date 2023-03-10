import cv2
import pickle
# NOTE: calibrate01 = RED:LEFT camera
with open("calibrate01.pkl", 'rb') as f:  # open a text file
    calibrate01 = pickle.load(f) # serialize the list

with open("calibrate02.pkl", 'rb') as f:  # open a text file
    calibrate02 = pickle.load(f) # serialize the list
width, height = 640,480

print(calibrate01.keys())
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
stereocalibration_flags = cv2.CALIB_FIX_INTRINSIC            #                            RED:left                  BLACK:right
ret, CM1, dist1, CM2, dist2, R, T, E, F = cv2.stereoCalibrate(calibrate01['objpoints'], calibrate01['imgpoints'], calibrate02['imgpoints'],
                                                              calibrate01['camMat'], calibrate01['Dist coeffs'],
                                                              calibrate02['camMat'], calibrate02['Dist coeffs'], 
                                                              (width, height), criteria = criteria, flags = stereocalibration_flags)

print(ret, CM1, dist1, CM2, dist2, R, T, E, F)