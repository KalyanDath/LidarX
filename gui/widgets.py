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
        icon_size = QSize(32, 32)  # Adjust the icon size as needed
        toggle_button.setIconSize(icon_size)
        toggle_button.setIcon(QIcon("gui/static/point_pick.png"))  # Set the path to your icon image
        toggle_button.setCheckable(True)
        toggle_button.clicked.connect(self.toggle_action)
        layout.addWidget(toggle_button)

    def toggle_action(self):
        if self.sender().isChecked():
            # Perform an action when the toggle button is selected
            self.main_window.plotter_widget.plotter.enable_point_picking(callback=lambda picked_point: point_picking(picked_point,self.main_window.plotter_widget.plotter),color='white',use_mesh=False)
            # Enable your point picking functionality here
        else:
            # Perform an action when the toggle button is deselected
            self.main_window.plotter_widget.plotter.disable_picking()
            # Disable your point picking functionality here