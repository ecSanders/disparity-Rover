import numpy as np
import cv2
import time

Cam= cv2.VideoCapture(1)
output_path = "./data/"

start = time.time()
T = 10
count = 0

while True:
    for t in range(4):
        print(f'{t} seconds')
        time.sleep(1)
        
    ret, frame= Cam.read()
    frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    frameL = frame[0:960, 1280:2560]
    frameR = frame[0:960, 0:1280]    
    
    cv2.imshow('imgR',frameL)
    cv2.imshow('imgL',frameR)

    # Find the chess board corners
    retR, cornersR = cv2.findChessboardCorners(frameL,(8,6),None)
    retL, cornersL = cv2.findChessboardCorners(frameR,(8,6),None)

    # If corners are detected in left and right image then we save it.
    if (retR == True) and (retL == True) and (frameL.shape[:2] == (960,1280)) and (frameR.shape[:2] == (960,1280)):
        print(count)
        count+=1
        cv2.imwrite(output_path+'stereoR/img%d.png'%count,frameR)
        cv2.imwrite(output_path+'stereoL/img%d.png'%count,frameL)
    
    # Press esc to exit
    if cv2.waitKey(1) & 0xFF == 27:
        print("Closing the cameras!")
        break

# Release the Cameras
Cam.release()
cv2.destroyAllWindows()