import open3d as o3d
import numpy as np

# Read a point cloud
cloud = o3d.data.PLYPointCloud()
pc = o3d.io.read_point_cloud('fragment.ply')

# Print and render the point cloud
print(pc)
print(np.asarray(pc.points))
o3d.visualization.draw_geometries([pc])