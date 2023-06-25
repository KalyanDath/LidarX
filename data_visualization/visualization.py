import pyvista as pv
import numpy as np
from data_visualization.optimize import optimized

def visualizer(las_file,plotter):
    x = las_file.x
    y = las_file.y
    z = las_file.z
    
    #Create Polydata from points in las file
    points = np.vstack((x,y,z)).transpose()
    cloud = pv.PolyData(points)

    if cloud.number_of_points >= 30000000:
        cloud = optimized(cloud)
        
    cloud.save("cloud.vtk")
    #Criteria to Color the points
    try:
        color_points = np.vstack((las_file.red, las_file.green, las_file.blue)).transpose()
        color_points = color_points/65335
        rgba= color_points - color_points.min(axis=0)
        rgba /= rgba.max(axis=0)
        cloud["color_by"] = rgba#color_points
    except:
        cloud["color_by"] = cloud.points[:,2]   #color by elevation

    
    actor = plotter.add_mesh(cloud, point_size=1,scalars="color_by", style="points",reset_camera=True,show_scalar_bar=False,name='point_cloud')
    plotter.disable_eye_dome_lighting()



    #toggle the point cloud for visibility
    def toggle_vis(flag):
        actor.SetVisibility(flag)
    _ = plotter.add_checkbox_button_widget(toggle_vis, value=True, size=35, color_on = 'green')
    
    plotter.show()
