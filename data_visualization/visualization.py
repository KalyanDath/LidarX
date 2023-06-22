import pyvista as pv
import numpy as np

def visualizer(las_file,plotter):
    x = las_file.x
    y = las_file.y
    z = las_file.z

    #Create Polydata from points in las file
    points = np.vstack((x,y,z)).transpose()
    cloud = pv.PolyData(points)
    
    #Criteria to Color the points
    try:
        color_points = np.vstack((las_file.red, las_file.green, las_file.blue)).transpose()
        color_points = color_points/65335
        rgba= color_points - color_points.min(axis=0)
        rgba /= rgba.max(axis=0)
        cloud["color_by"] = rgba#color_points
    except:
        cloud["color_by"] = z

    plotter.clear()
    plotter.add_mesh(cloud,scalars="color_by", point_size=1, style="points",reset_camera=True,show_scalar_bar=False)
    plotter.disable_eye_dome_lighting()
    
    plotter.show()
