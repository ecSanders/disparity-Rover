import torch
import cv2

#Initalize constants
COLOR = (0,255,255)
THICKNESS = 2

# Load model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load image
img = cv2.imread("../../Images/stitch01_med.jpg")

# Run inference
results = model(img)

df = results.pandas().xyxy[0]

for obj in df.iterrows():
    top_right = (int(obj[1][0]), int(obj[1][1]))
    bottom_left = (int(obj[1][2]), int(obj[1][3]))
    img = cv2.rectangle(img, top_right, bottom_left, COLOR, THICKNESS)

cv2.imshow("Test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()