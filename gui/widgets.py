from PyQt5.QtWidgets import QWidget, QVBoxLayout,QPushButton
from pyvistaqt import QtInteractor
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from data_visualization.pick_point import point_picking


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
            self.main_window.plotter_widget.plotter.enable_point_picking(callback=lambda picked_point: point_picking(picked_point,self.main_window.plotter_widget.plotter,True),show_point=False)
            
        else:
            # Perform an action when the toggle button is deselected
            point_picking([],self.main_window.plotter_widget.plotter,False)
            self.main_window.point_distance.setEnabled(True)


class point_distance_widget(QWidget):
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
                background-color: #2ecc71;
                color: #ffffff;
                border-radius: 5px;
                border: none;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
            QPushButton:checked {
                background-color: #27ae60;
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
            self.main_window.pick_point.setEnabled(False)
            self.main_window.plotter_widget.plotter.enable_path_picking(callback=None,color="red")
            # Perform an action when the toggle button is selected
            pass
        else:
            self.main_window.pick_point.setEnabled(True)
            self.main_window.plotter_widget.plotter.disable_picking()
            # Perform an action when the toggle button is deselected
            