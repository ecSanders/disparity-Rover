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
retS, new_mtxL, distL, new_mtxR, distR, Rot, Trns, Emat, Fmat = cv2.stereoCalibrate(calibrate01['objpoints'], calibrate01['imgpoints'], calibrate02['imgpoints'],
                                                              calibrate01['camMat'], calibrate01['Dist coeffs'],
                                                              calibrate02['camMat'], calibrate02['Dist coeffs'], 
                                                              (width, height), criteria = criteria, flags = stereocalibration_flags)

# print(ret, CM1, dist1, CM2, dist2, R, T, E, F)


rectify_scale= 1
rect_l, rect_r, proj_mat_l, proj_mat_r, Q, roiL, roiR= cv2.stereoRectify(new_mtxL, distL, new_mtxR, distR, imgL_gray.shape[::-1], Rot, Trns, rectify_scale,(0,0))