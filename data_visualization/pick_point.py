picked_points=[]
text_actor=None
def point_picking(points,plotter):
    global picked_points
    global text_actor
    print(points)

    if text_actor is not None:
        plotter.remove_actor(text_actor)   

    text_actor = plotter.add_text(f"Picked Point:\nX:{points[0]:.2f}\nY:{points[1]:.2f}\nZ:{points[2]:.2f}",position="upper_right",font_size=12)
