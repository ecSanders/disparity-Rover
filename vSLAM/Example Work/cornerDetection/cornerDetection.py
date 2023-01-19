import cv2 as cv
import numpy as np

# Read in an image file
filename = 'chair.png'
img = cv.imread(filename)

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Set data type to 32-bit floating point
gray = np.float32(gray)

# Apply Harris Corner Detection to detect corners
dst = cv.cornerHarris(gray, 2, 3, 0.04)

# Mark results with dilated corners
dst = cv.dilate(dst, None)

# Revert to original image with optimal threshold value
img[dst > 0.01 * dst.max()] = [0, 0, 255]

# Display output image in window
cv.imshow('dst', img)

# De-allocate any associated memory usage
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()