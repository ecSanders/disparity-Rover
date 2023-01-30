'''
Title: display.py
Authors: Jared Perlic
Date Start: Jan 30, 2023
Description:

This script displays a point cloud
'''
import open3d as o3d
import numpy as np

PATH = "../../Pointclouds"

# Read a point cloud
cloud = o3d.data.PLYPointCloud()
pcd = o3d.io.read_point_cloud(PATH +'fragment.ply')

# Print and render the point cloud
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])