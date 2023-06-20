from PyQt5.QtWidgets import QToolBar
from PyQt5.QtGui import QIcon
from data_visualization.views import front_view
from gui.widgets import point_picking_widget
from PyQt5.QtCore import QSize

def create_toolbar(main_window):
    toolbar = QToolBar(main_window)
    main_window.addToolBar(toolbar)

    # Add the buttons with icons to the toolbar
    toolbar.addAction(QIcon("path/to/top_view_icon.png"), "Top View")
    toolbar.addAction(QIcon("path/to/bottom_view_icon.png"), "Bottom View")
    # Add other toolbar actions
    pick_point = point_picking_widget(main_window)
    toolbar.addWidget(pick_point)
