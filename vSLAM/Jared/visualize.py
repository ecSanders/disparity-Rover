import open3d as o3d
import numpy as np

# Cast random points to a 3-column numpy array
xyz = np.random.rand(100, 3)

# Pass array to Open3D.o3d.geometry.PointCloud and visualize
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz)
o3d.io.write_point_cloud('data.ply', pcd)