import cv2 as cv

openCvVidCapIds = []

for i in range(100):
    try:
        cap = cv.VideoCapture(i)
        if cap is not None and cap.isOpened():
            openCvVidCapIds.append(i)
    except:
        pass

print(str(openCvVidCapIds))