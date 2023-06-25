import math
import numpy as np
import pyvista as pv
picked_points,point_actors,text_actors=[],[],[]
status=False
def distance_calculation(points, plotter):
    global picked_points,point_actors,text_actors,status,line_actor,dist_actor
    if status:
        for actor in point_actors:
            plotter.remove_actor(actor)
        for actor in text_actors:
            plotter.remove_actor(actor)
        plotter.remove_actor(line_actor)
        plotter.remove_actor(dist_actor)
        status=False
        picked_points=[]
        point_actors,text_actors=[],[]

    point_actor = plotter.add_mesh(pv.PolyData(points), color='red', point_size=10, style='points',reset_camera=False,render_points_as_spheres=True)
    point_actors.append(point_actor)
    picked_points.append(points)

    text_actor = plotter.add_point_labels(points,[f"Picked Point:\n  X:{points[0]:.2f}\n  Y:{points[1]:.2f}\n  Z:{points[2]:.2f}"],font_size=24,show_points=False,shape_color="black",shape_opacity=0.8,always_visible=True,text_color="#CCCCCC")
    text_actors.append(text_actor)

    if len(picked_points)==2:
        points1=np.array(picked_points)
        x=(picked_points[0][0]-picked_points[1][0])**2
        y=(picked_points[0][1]-picked_points[1][1])**2
        z=(picked_points[0][2]-picked_points[1][2])**2
        dist=math.sqrt(x+y+z)
        line_actor=plotter.add_lines(points1,color='red')
        midpoint=[]
        midpoint.append((picked_points[0][0]+picked_points[1][0])/2)
        midpoint.append((picked_points[0][1]+picked_points[1][1])/2)
        midpoint.append((picked_points[0][2]+picked_points[1][2])/2)
        dist_actor = plotter.add_point_labels(midpoint, [f"Distance: {dist:.4f}"], font_size=24, show_points=False,
                                              shape_color="black", shape_opacity=0.8, always_visible=True,
                                              text_color="#CCCCCC")
        status=True
