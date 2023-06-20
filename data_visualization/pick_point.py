import pyvista as pv
picked_points=[]
text_actor=None
point_actor=None
def point_picking(points,plotter,status):
    global picked_points
    global text_actor
    global point_actor

    if status== False:
        plotter.remove_actor(text_actor)
        plotter.remove_actor(point_actor)
        picked_points=[]
    else:
        picked_points.append(points)

        if text_actor is not None:
            plotter.remove_actor(text_actor)
            plotter.remove_actor(point_actor)
        
        point_actor = plotter.add_mesh(pv.PolyData(points), color='red', point_size=10, style='points',reset_camera=False,render_points_as_spheres=True)
        text_actor = plotter.add_text(f"Picked Point:\nX:{points[0]:.2f}\nY:{points[1]:.2f}\nZ:{points[2]:.2f}",position="lower_left",font_size=16,shadow=True)
