import open3d as o3d

# Obtain the eagle point cloud
eagle = o3d.data.EaglePointCloud()
pcd_eagle = o3d.io.read_point_cloud(eagle.path)

# Obtain the bunny mesh
bunny = o3d.data.BunnyMesh()
mesh_bunny = o3d.io.read_triangle_mesh(bunny.path)
mesh_bunny.compute_vertex_normals()

# Turn bunny mesh into bunny point cloud
pcd_bunny = mesh_bunny.sample_points_poisson_disk(750) 

# Function used to construct a mesh using the Poisson algorithm
# pcd: o3d point cloud object
# filename: file to be saved in
# depth: depth of Poisson tree, parameter to be experimented with
def construct_mesh_poisson(pcd, filename, depth):
    print(pcd)
    # draw original pointcloud
    o3d.visualization.draw_geometries([pcd])

    with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
        # generate mesh
        mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=depth)
        print(mesh)
        # draw mesh
        o3d.visualization.draw_geometries([mesh])
        # save to file
        o3d.io.write_triangle_mesh(filename, mesh, 
                write_triangle_uvs=True)

# Function used to construct a mesh using the Poisson algorithm
# pcd: o3d point cloud object
# filename: file to be saved in
# alpha: alpha parameter, to be experimented with
def construct_mesh_alpha(pcd, filename, alpha):
    print(pcd)
    # draw point cloud
    o3d.visualization.draw_geometries([pcd])
    with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
        # compute mesh
        mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha)
        mesh.compute_vertex_normals()
        print(mesh)
        # draw mesh
        o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)
        # save to file
        o3d.io.write_triangle_mesh(filename, mesh, 
                write_triangle_uvs=True)

# Function used to construct a mesh using the Poisson algorithm
# pcd: o3d point cloud object
# filename: file to be saved in
# radii: Python list of potential ball radii, parameter for experimentation
def construct_mesh_ball_pivot(pcd, filename, radii):
    print(pcd)
    # draw point cloud
    o3d.visualization.draw_geometries([pcd])
    # compute mesh
    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
            pcd, o3d.utility.DoubleVector(radii))
    print(mesh)
    # draw mesh
    o3d.visualization.draw_geometries([mesh])
    # save to file
    o3d.io.write_triangle_mesh(filename, mesh, 
                write_triangle_uvs=True)



# The following lines generate meshes using default open3d data with
# different parameters. Feel free to experiment if you want.

#construct_mesh_poisson(pcd_eagle, 'eagle_mesh.glb', 9)
#construct_mesh_poisson(pcd_bunny, 'bunny_mesh_poisson.glb')
#construct_mesh_alpha(pcd_eagle, 'eagle_mesh_alpha.glb', 0.03)
#construct_mesh_alpha(pcd_bunny, 'bunny_mesh_alpha.glb', 0.02)
#construct_mesh_ball_pivot(pcd_bunny, 'bunny_mesh_ballpiv.glb', [0.005, 0.01, 0.015, 0.02, 0.03])
