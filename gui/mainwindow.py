from PyQt5.QtWidgets import QMainWindow,QVBoxLayout, QWidget, QMenuBar, QAction, QFileDialog, QToolBar
from PyQt5.QtGui import QIcon
from gui.widgets import PlotterWidget
import os
from data_visualization.views import front_view
from gui.menu_bar import create_menu_bar
from gui.toolbar import create_toolbar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenLidarX")
        self.setWindowIcon(QIcon("gui/static/speed-camera.png"))
        self.setMinimumSize(800, 600) 
        self.showMaximized()
        

        self.central_widget = QWidget(self) 
        self.setCentralWidget(self.central_widget)
        main_layout = QVBoxLayout(self.central_widget)
        
        #create the plotter widget
        self.plotter_widget = PlotterWidget()
        main_layout.addWidget(self.plotter_widget)

        #create the menu bar
        create_menu_bar(self)   #self.create_menu_bar()

        #create a toolbar
        create_toolbar(self)    #self.create_toolbar()