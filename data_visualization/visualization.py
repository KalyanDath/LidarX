import pyvista as pv
import numpy as np

def visualizer(las_file,plotter):
    x = las_file.x
    y = las_file.y
    z = las_file.z

   # color_points = np.vstack((las_file.red, las_file.green, las_file.blue)).transpose()

   # colors = np.sum(color_points, axis=1)
    points = np.column_stack((x,y,z))
    
    cloud = pv.PolyData(points)
    cloud["elevation"]  =z# colors
    #print(colors)
    #print(colors)
    plotter.clear()
    #intensity_range = (colors.min(), colors.max())
    plotter.disable_anti_aliasing()  #performance 
    plotter.add_mesh(cloud, cmap = "jet" ,scalars="elevation", point_size=1, style="points",reset_camera=True,n_colors=65336)
    plotter.disable_eye_dome_lighting()
    #plotter.remove_scalar_bar()


    plotter.show()