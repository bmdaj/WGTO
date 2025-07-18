import trimesh
import numpy as np
import plotly.graph_objects as go

def export_mesh(path, var, scaling, t, preview=False):
    ny, nx = var.shape    
    pattern_boxes = []
    for y in range(ny):
        for x in range(nx):
            if var[y, x] > 0.5:
                box = trimesh.creation.box(extents=(scaling, scaling, t),
                                        transform=trimesh.transformations.translation_matrix([
                                            x * scaling + scaling / 2,
                                            y * scaling + scaling / 2,
                                            0
                                        ]))
                pattern_boxes.append(box)
    
    # Combine all geometry
    all_parts = pattern_boxes
    #model = trimesh.util.concatenate(all_parts)
    model = trimesh.boolean.union(all_parts, engine='manifold')
    if preview:
        # Preview the mesh in 3D
        preview_mesh(model)
    # Export the mesh to an STL file
    model.export(path, file_type='stl')
    
def preview_mesh(model):
    # --- Plotly 3D viewer ---
    vertices = model.vertices
    faces = model.faces
    fig = go.Figure(data=[
        go.Mesh3d(
            x=vertices[:, 0],
            y=vertices[:, 1],
            z=vertices[:, 2],
            i=faces[:, 0],
            j=faces[:, 1],
            k=faces[:, 2],
            opacity=0.7,
            color='lightblue',
            flatshading=True
        )
    ])
    fig.update_layout(
        scene=dict(aspectmode='data'),
        title="3D Mesh Preview",
        margin=dict(l=0, r=0, t=30, b=0)
    )
    fig.show()