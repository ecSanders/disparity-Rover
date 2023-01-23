import open3d as o3d
import numpy as np

# Declare numpy array
arr = np.random.rand(100, 3)

# Pass array to Open3D.o3d.geometry.PointCloud and visualize
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(arr)
o3d.io.write_point_cloud("./data.ply", pcd)