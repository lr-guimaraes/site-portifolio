import open3d as o3d
pcd = o3d.io.read_point_cloud("source_pointcloud.ply")
o3d.io.write_point_cloud("sink_pointcloud.pcd", pcd)