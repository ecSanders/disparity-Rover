import cv2 as cv

# Define a VideoCapture object
vid = cv.VideoCapture(0)

while True:

    # Capture video frame by frame
    ret, frame = vid.read()

    # Display the frame
    cv.imshow('frame', frame)

    # Press `q` to close the window
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
vid.release()

cv.destroyAllWindows()