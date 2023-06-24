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
        plotter.disable_picking()
    else:
        picked_points.append(points)

        if text_actor is not None:
            plotter.remove_actor(text_actor)
            plotter.remove_actor(point_actor)
        
        point_actor = plotter.add_mesh(pv.PolyData(points), color='red', point_size=10, style='points',reset_camera=False,render_points_as_spheres=True)
        text_actor = plotter.add_point_labels(points,[f"Picked Point:\n  X:{points[0]:.2f}\n  Y:{points[1]:.2f}\n  Z:{points[2]:.2f}"],font_size=24,show_points=False,shape_color="black",shape_opacity=0.8,always_visible=True,text_color="#88cc00")
