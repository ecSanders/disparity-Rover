'''
Title: main.py
Authors: Erik Sanders, Jared Perlic, Tyson Mergle
Date Start: Jan 12, 2023
Description:

This file is meant to run all the core components that makeup the 
visual SLAM algorithm. The process that is used is as follows:

1. Map Initialization
- Detect
- Extract
- Match
- Estimate relative camera pose from matched feature points
- Find 3-D locations of the matched feature points
- Refine initial map
- Manage data for initial map and key frames

2. Tracking
- Match extracted features
- Estimate camera pose
- Project map points
- Search for feature correspondences
- Refine camera pose
- Identify local map points
- Search for more feature correspondences
- Refine camera pose 
- Store new key frame

3. Local Mapping
- Connect key frames 
- Search for matches in connected key frames
- Compute location for new matches
- Store new map points
- Store 3-D to 2-D correspondences
- Update odometry connection
- Store representative view of 3-D points
- Store distance limits and viewing direction of 3-D points 
- Refine pose
- Remove outliers

4. Loop Detection
- Construct bag of visual words
- Create recognition database
- Identify loop closure candidates
- Compute relative camera pose for loop closure candidates
- Close loop

5. Drift Correction

6. Visualization
'''


def driver():
    pass

if __name__ == '__main__':
    driver()