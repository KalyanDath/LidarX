from PyQt5.QtWidgets import QWidget, QVBoxLayout,QPushButton
from pyvistaqt import QtInteractor
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from data_visualization.pick_point import PointPicker
from data_visualization.point_distance import PointDistance
from data_visualization.decimation import decimate


class PlotterWidget(QWidget):
    def __init__(self):
        super().__init__()  
        self.plotter = QtInteractor(self)
        self.plotter.set_background('black', top="#0a6595")
        self.plotter.add_camera_orientation_widget()
        layout = QVBoxLayout()
        layout.addWidget(self.plotter)
        self.setLayout(layout)

class point_picking_widget(QWidget):
    def __init__(self,mainwindow):
        self.main_window = mainwindow
        super().__init__()
        self.initUI()
        self.point_picker = None

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create the toggle button with an icon
        toggle_button = QPushButton()
        toggle_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: #ffffff;
                border-radius: 5px;
                border: none;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:checked {
                background-color: #2980b9;
            }
        """)
        icon_size = QSize(32, 32)  # Adjust the icon size as needed
        toggle_button.setIconSize(icon_size)
        toggle_button.setIcon(QIcon("gui/static/point_pick.png"))  # Set the path to your icon image
        toggle_button.setCheckable(True)
        toggle_button.clicked.connect(self.toggle_action)
        layout.addWidget(toggle_button)


    def toggle_action(self):
        if self.sender().isChecked():
            
            # Perform an action when the toggle button is selected
            self.main_window.point_distance.setEnabled(False)
            self.point_picker = PointPicker(self.main_window.plotter_widget.plotter)
            self.main_window.plotter_widget.plotter.enable_point_picking(callback=self.point_picker.point_picking,
                                                                         show_point=False)
            
        else:
            # Perform an action when the toggle button is deselected
            self.point_picker.disable()
            self.main_window.point_distance.setEnabled(True)


class point_distance_widget(QWidget):
    def __init__(self,mainwindow):
        self.main_window = mainwindow
        super().__init__()
        self.initUI()
        self.point_distance = None

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create the toggle button with an icon
        toggle_button = QPushButton()
        toggle_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: #ffffff;
                border-radius: 5px;
                border: none;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #1b7a43;
            }
            QPushButton:checked {
                background-color: #1b7a43;
            }
        """)
        icon_size = QSize(32, 32)  # Adjust the icon size as needed
        toggle_button.setIconSize(icon_size)
        toggle_button.setIcon(QIcon("gui/static/point_distance.png"))  # Set the path to your icon image
        toggle_button.setCheckable(True)
        toggle_button.clicked.connect(self.toggle_action)
        layout.addWidget(toggle_button)

    def toggle_action(self):
        if self.sender().isChecked():
            # Perform an action when the toggle button is selected
            self.main_window.pick_point.setEnabled(False)
            self.point_distance = PointDistance(self.main_window.plotter_widget.plotter)
            self.main_window.plotter_widget.plotter.enable_point_picking(callback=self.point_distance.distance_plot,
                                                                         show_point=False)
        else:
            # Perform an action when the toggle button is deselected
            self.main_window.pick_point.setEnabled(True)
            self.point_distance.disable()
            
class decimate_cloud_widget(QWidget):
    def __init__(self,mainwindow):
        self.main_window = mainwindow
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create the toggle button with an icon
        toggle_button = QPushButton()
        toggle_button.setStyleSheet("""
            QPushButton {
                background-color:  #8e44ad;
                color: #ffffff;
                border-radius: 5px;
                border: none;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #6c3483;;
            }
            QPushButton:checked {
                background-color:  #6c3483;
            }
        """)
        icon_size = QSize(32, 32)  # Adjust the icon size as needed
        toggle_button.setIconSize(icon_size)
        toggle_button.setIcon(QIcon("gui/static/cloud_decimate.png"))  # Set the path to your icon image
        toggle_button.setCheckable(True)
        toggle_button.clicked.connect(self.toggle_action)
        layout.addWidget(toggle_button)

    def toggle_action(self):
        if self.sender().isChecked():
            # Perform an action when the toggle button is selected
            self.main_window.pick_point.setEnabled(False)
            decimate(self.main_window.plotter_widget.plotter)
            
        else:
            # Perform an action when the toggle button is deselected
            self.main_window.pick_point.setEnabled(True)
            self.main_window.plotter_widget.plotter.clear_slider_widgets()
            