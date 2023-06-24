
def remove_filter(plotter):

    plotter.disable_eye_dome_lighting()
    plotter.disable_ssao()
    plotter.disable_anti_aliasing()

def edl_shader(plotter):
    plotter.enable_eye_dome_lighting()
    

def ssao_shader(plotter):
    plotter.enable_ssao(kernel_size=128)
    plotter.enable_anti_aliasing('ssaa')
    
