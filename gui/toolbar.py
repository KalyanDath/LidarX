from PyQt5.QtWidgets import QToolBar,QPushButton
from PyQt5.QtGui import QIcon
import data_visualization.views as views
from gui.widgets import point_picking_widget,point_distance_widget
from PyQt5.QtCore import QSize

def create_toolbar(main_window):
    toolbar = QToolBar(main_window)
    main_window.addToolBar(toolbar)
    #toolbar.setStyleSheet("background-color: white;")

    # Add the buttons with icons to the toolbar
    toolbar.addAction(QIcon("gui/static/front-view.png"), "Set Front View",lambda: views.front_view(main_window.plotter_widget.plotter))
    toolbar.addAction(QIcon("gui/static/back-view.png"), "Set Back View",lambda: views.back_view(main_window.plotter_widget.plotter))
    toolbar.addAction(QIcon("gui/static/left-view.png"), "Set Left View",lambda: views.left_side_view(main_window.plotter_widget.plotter))
    toolbar.addAction(QIcon("gui/static/right-view.png"), "Set Right View",lambda: views.right_side_view(main_window.plotter_widget.plotter))
    toolbar.addAction(QIcon("gui/static/top-view.png"), "Set Top View",lambda: views.top_view(main_window.plotter_widget.plotter))
    toolbar.addAction(QIcon("gui/static/bottom-view.png"), "Set Bottom View",lambda: views.bottom_view(main_window.plotter_widget.plotter))
    toolbar.addAction(QIcon("gui/static/front-isometric.png"), "Set Front Isometric View",lambda: views.front_isometric_view(main_window.plotter_widget.plotter))
    toolbar.addAction(QIcon("gui/static/back-isometric.png"), "Set Back Isometric View",lambda: views.back_isometric_view(main_window.plotter_widget.plotter))
    # Add other toolbar actions
    pick_point = point_picking_widget(main_window)
    toolbar.addWidget(pick_point)

    point_distance = point_distance_widget(main_window)
    toolbar.addWidget(point_distance)


    
    return (pick_point,point_distance)
    