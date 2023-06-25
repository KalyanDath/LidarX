import pyvista as pv
import numpy as np

def decimate_cloud(slider_value,plotter):
    cloud = pv.read('cloud.vtk')
    #Set the reduction ratio to be the value of the slider.
    slider_value = round(slider_value,2)
    reduction_ratio = slider_value/100
    old_points_num = cloud.number_of_points
    new_points_num = int(old_points_num * reduction_ratio)
    downsampled_indices = np.random.choice(old_points_num , new_points_num, replace=False)
    new_cloud_points = cloud.points[downsampled_indices]
    new_cloud = pv.PolyData(new_cloud_points)
    new_cloud["color_by"] = new_cloud.points[:,2]
    plotter.add_mesh(new_cloud,point_size=1,scalars='color_by',style="points",name='point_cloud',reset_camera=False,show_scalar_bar=False)

def decimate(plotter):
    plotter.add_slider_widget(lambda slider_value: decimate_cloud(slider_value,plotter),[1,100], title="Reduction Ratio", value=50, color="white")
