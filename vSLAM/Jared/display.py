import open3d as o3d
import numpy as np

# Read a point cloud
cloud = o3d.data.PLYPointCloud()
pcd = o3d.io.read_point_cloud('fragment.ply')

# Print and render the point cloud
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])