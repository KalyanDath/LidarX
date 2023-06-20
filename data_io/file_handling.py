import os
import laspy
import numpy as np
from data_visualization import visualization

def read_file(file_path, plotter):
    file_extension = os.path.splitext(file_path)[1]

    if file_extension ==  ".las":
        process_las_file(file_path,plotter)
    else:
        pass

def process_las_file(file_path,plotter):
    las_file = laspy.read(file_path)
    plotter.reset_camera()
    visualization.visualizer(las_file,plotter)

    #return las_details