# https://www.loom.com/share/eee8d4c2231943e8a54d2109c1c16b6f
try:
    import os
    import cv2
    import numpy as np
    from obj_detection import detect
except:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    os.system("pip install -r requirements.txt")

def main(cam, stereo):
    # Initiate ORB detector
    orb = cv2.ORB_create()

    while True:
        ### FRAME 01 ###

        # Get frames
        retL, frame = cam.read()

        left = frame[0:960, 1280:2560]
        right = frame[0:960, 0:1280]

        # Find keypoints and descriptors
        kp1, des1 = orb.detectAndCompute(left, None)
        kp2, des2 = orb.detectAndCompute(right, None)

        # Create BFMatcher object
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Match descriptors
        matches = bf.match(des1, des2)

        # Make sure at least 15 feature matches were found
        assert len(matches) >= 5

        # Sort them in the order of their distance
        matches = sorted(matches, key=lambda x:x.distance)

        # Draw first 10 matches
        img3 = cv2.drawMatches(left, kp1, right, kp2, matches[:5], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

        # Detect objects (COCO images)
        left_det = detect(img3)

        #Resize to view
        sized = cv2.resize(left_det, (1280, 480))

        cv2.imshow("Camera Feed", sized)

        ### FRAME 02 ###
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        imgL_gray = img_gray[0:960, 1280:2560]
        imgR_gray = img_gray[0:960, 0:1280]

        # Apply stereo image rectification on the left image
        Left_nice = cv2.remap(imgL_gray,
                             Left_Stereo_Map_x,
                             Left_Stereo_Map_y,
                             cv2.INTER_LINEAR,
                             0)


        # Apply stereo image rectification on the right image
        Right_nice = cv2.remap(imgR_gray,
                              Right_Stereo_Map_x,
                              Right_Stereo_Map_y,
                              cv2.INTER_LINEAR,
                              0)

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
        cv2.imshow("disp", disparity)

        # Press `q` to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()

    cv2.destroyAllWindows()




if __name__ == "__main__":
    # Read and map values for stereo image rectification
    cv_file = cv2.FileStorage("data/params_py.xml", cv2.FILE_STORAGE_READ)
    Left_Stereo_Map_x = cv_file.getNode("Left_Stereo_Map_x").mat()
    Left_Stereo_Map_y = cv_file.getNode("Left_Stereo_Map_y").mat()
    Right_Stereo_Map_x = cv_file.getNode("Right_Stereo_Map_x").mat()
    Right_Stereo_Map_y = cv_file.getNode("Right_Stereo_Map_y").mat()
    cv_file.release()

    # Create an object of StereoBM algorithm

    minDisparity=30
    numDisparities=160
    stereo = cv2.StereoBM_create(numDisparities=numDisparities, blockSize=5)

    cam = cv2.VideoCapture(1)  # Camera ID for left camera

    main(cam, stereo)