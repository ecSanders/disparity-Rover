import cv2
import numpy as np

# Read in an image file
filename = 'chair.png'
img = cv2.imread(filename)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set data type to 32-bit floating point
gray = np.float32(gray)

# Apply Harris Corner Detection to detect corners
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Mark results with dilated corners
dst = cv2.dilate(dst, None)

# Revert to original image with optimal threshold value
img[dst > 0.01 * dst.max()] = [0, 0, 255]

# Display output image in window
cv2.imshow('dst', img)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()