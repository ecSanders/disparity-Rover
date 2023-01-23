import cv2 as cv
import numpy as np
import imutils
import time

# Get file names
files = 'stitch01_small.jpg stitch02_small.jpg'  # Small images aren't stitched significantly faster

# Load images into list
imgs = [cv.imread(f'../../Images/{file}') for file in files.split(' ')]

# # View images
# for img in imgs:
#     cv.imshow(f"Image", img)

#     cv.waitKey(0)
#     cv.destroyAllWindows()

# Create stitching object
stitcher = cv.Stitcher.create(cv.Stitcher_SCANS)
stitcher.setPanoConfidenceThresh(0.0)

# Start the timer
start = time.time()

# Perform the stitch
(status, res) = stitcher.stitch(imgs)

# Stop the timer
stop = time.time()

# Make sure it was successful
assert status == 0

cv.imshow('Result', res)
cv.waitKey(0)
cv.destroyAllWindows()

# Print the time taken to stitch
print(f'Time to stitch: {round(stop - start, 2)}s')