import cv2 as cv

# Define a VideoCapture object
cam = cv.VideoCapture(0)

while True:

    # Capture video frame by frame
    ret, frame = cam.read()

    # Display the video
    cv.imshow('disp', frame)

    # Press `q` to close the window
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cam.release()

cv.destroyAllWindows()