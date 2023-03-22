import numpy as np
import cv2
import time

print("Checking the right and left camera IDs:")
print("Press (y) if IDs are correct and (n) to swap the IDs")
print("Press enter to start the process >> ")
input()

# Check for left and right camera IDs



# for i in range(100):
#     retL, frameL= Cam.read()

# cv2.imshow('imgL',frameL)

# if cv2.waitKey(0) & 0xFF == ord('y') or cv2.waitKey(0) & 0xFF == ord('Y'):
#     CamL_id = 0
#     CamR_id = 2
#     print("Camera IDs maintained")

# elif cv2.waitKey(0) & 0xFF == ord('n') or cv2.waitKey(0) & 0xFF == ord('N'):
#     CamL_id = 2
#     CamR_id = 0
#     print("Camera IDs swapped")
# else:
#     print("Wrong input response")
#     exit(-1)
# CamR.release()
# CamL.release()

Cam= cv2.VideoCapture(1)
# CamL= cv2.VideoCapture(CamL_id)
# CamR= cv2.VideoCapture(CamR_id)
output_path = "./data/"

start = time.time()
T = 10
count = 0

while True:
    # timer = T - int(time.time() - start)
    ret, frame= Cam.read()

    frameL = frame[0:960, 1281:2560]
    frameR = frame[0:960, 0:1280]    
    
    # img1_temp = frameL.copy()
    # cv2.putText(img1_temp,"%r"%timer,(50,50),1,5,(55,0,0),5)

    grayR= cv2.cvtColor(frameR,cv2.COLOR_BGR2GRAY)
    grayL= cv2.cvtColor(frameL,cv2.COLOR_BGR2GRAY)
    cv2.imshow('imgR',grayR)
    cv2.imshow('imgL',grayL)

    # Find the chess board corners
    retR, cornersR = cv2.findChessboardCorners(grayR,(9,10),None)
    retL, cornersL = cv2.findChessboardCorners(grayL,(9,10),None)

    print(retR, retL)
    # If corners are detected in left and right image then we save it.
    if (retR == True) and (retL == True):
        print("FOUND!")
        count+=1
        cv2.imwrite(output_path+'stereoR/img%d.png'%count,frameR)
        cv2.imwrite(output_path+'stereoL/img%d.png'%count,frameL)
    
    # if timer <=0:
    #     start = time.time()
    
    # Press esc to exit
    if cv2.waitKey(1) & 0xFF == 27:
        print("Closing the cameras!")
        break

# Release the Cameras
Cam.release()
cv2.destroyAllWindows()