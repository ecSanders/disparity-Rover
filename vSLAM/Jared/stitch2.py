import stitching
import time

img_path = '../../Images'

# Create a Stitcher
settings = {'detector': 'sift', 'confidence_threshold': 0.2}
stitcher = stitching.Stitcher(**settings)

# Start the timer
start = time.time()

# Perform the stitch
res = stitcher.stitch(['{img_path}/stitch01_small.jpg', '{img_path}/stitch02_small.jpg'])

# Stop the timer
stop = time.time()

# Print the time taken to stitch
print(f'Time to stitch: {round(stop - start, 2)}s')