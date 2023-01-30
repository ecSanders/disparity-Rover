"""
NOTE: This code is intellectual property of 
"""

import cv2
import imutils
import numpy as np
import time

# Get file names
# files = "stitch01_small.jpg stitch02_small.jpg stitch03_small.jpg"
files = "stitch01_med.jpg stitch02_med.jpg"

# load images into list
imgs = [cv2.imread(f"../../Images/{file}") for file in files.split(" ")]
# Convert to Grayscale
# imgs = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in imgs]

# View images
# for img in imgs:
#     cv2.imshow(f"Image", img)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# Create stitching object
stitcher = cv2.Stitcher.create(cv2.Stitcher_SCANS)
# stitcher.setPanoConfidenceThresh(0.0)

# Stitch
start = time.time()
(status, stitched) = stitcher.stitch(imgs)
end = time.time()
# Make sure it was successful
assert status == 0
print(f'Stitching took: {end - start}')

cv2.imshow("Successful Stitch", stitched)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(f"../../Images/STITCHED.jpg", stitched)

### EXTRA STEPS TO GET CLEAN IMAGE ### 
# if status == 0:

#     # Create borders for stitching
#     stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10,
#     cv2.BORDER_CONSTANT, (0, 0, 0))

#     # Grayscale and threshold it: values > 0 -> 255
#     gray = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
#     thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

#     # Create and grab contours
#     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
#     cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     c = max(cnts, key=cv2.contourArea)

#     # Create rect using thresh??
#     mask = np.zeros(thresh.shape, dtype="uint8")
#     (x, y, w, h) = cv2.boundingRect(c)
#     cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

#     # Create mask copies
#     minRect = mask.copy()
#     sub = mask.copy()

#     while cv2.countNonZero(sub) > 0:

#         minRect = cv2.erode(minRect, None)
#         sub = cv2.subtract(minRect, thresh)

#         cnts = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL,
#                                 cv2.CHAIN_APPROX_SIMPLE)
#         cnts = imutils.grab_contours(cnts)
#         c = max(cnts, key=cv2.contourArea)
#         (x, y, w, h) = cv2.boundingRect(c)
#         # use the bounding box coordinates to extract the our final
#         # stitched image
#         stitched = stitched[y:y + h, x:x + w]

#     # write the output stitched image to disk
#     cv2.imwrite(f"../../Images/STITCHED.jpg", stitched)
#     # display the output stitched image to our screen
#     cv2.imshow("Stitched", stitched)
#     cv2.waitKey(0)