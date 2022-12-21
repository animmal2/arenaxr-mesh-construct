import open3d as o3d
from arena import *

scene = Scene(host = "arenaxr.org", scene = "point_mesh");
center = Position(0, 0, 2)

@scene.run_once
def main():
    # replace the names/ids/urls with whatever is appropriate
    eagle_mesh = GLTF(
            object_id="xr-logo",
            position=(0, 0, 2),
            scale=(1, 1, 1),
            url="bunny_mesh_ballpiv_filled.glb",)
    scene.add_object(eagle_mesh)


scene.run_tasks()
