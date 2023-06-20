def front_view(plotter):
    plotter.camera.azimuth = 180
    plotter.camera_position = "xz"

def bottom_view(plotter):
    plotter.camera.roll = 0 
    plotter.camera_position = "yx"

def back_isometric_view(plotter):
    plotter.camera_position = "iso"

def front_isometric_view(plotter):
    plotter.camera_position = "iso"
    plotter.camera.azimuth = 180
    

def left_side_view(plotter):
    plotter.camera.azimuth = 180
    plotter.camera_position = "yz"
    
def right_side_view(plotter):
    plotter.camera_position = "yz"

def top_view(plotter):
    plotter.camera_position = "xy"

#requires change in back_view
def back_view(plotter):
    plotter.camera_position = "yx"
    plotter.camera.roll = 0
    