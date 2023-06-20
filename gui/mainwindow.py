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



#######################################################################    
'''
    def create_menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        self.create_file_menu(menu_bar)
        self.create_display_menu(menu_bar)

    def create_file_menu(self,menu_bar):
        file_menu = menu_bar.addMenu("File")

        self.create_open_action(file_menu)

    def create_open_action(self,file_menu):
        open_action = QAction(QIcon("gui/static/open-folder.png"),"Open",self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

    def create_display_menu(self,menu_bar):
        display_menu = menu_bar.addMenu("Display")
        shader_filters_menu = display_menu.addMenu("Shader && Filters")
        shader_filters_menu.setIcon(QIcon("gui/static/shader.png"))

        action1 = QAction("Remove Filters ", self)
        action2 = QAction("EDL Shader", self)
        action3 = QAction("SSAO Shader", self)

        shader_filters_menu.addAction(action1)
        shader_filters_menu.addAction(action2)
        shader_filters_menu.addAction(action3)

        action1.triggered.connect(lambda: remove_filter(self.plotter_widget.plotter))
        action2.triggered.connect(lambda: edl_shader(self.plotter_widget.plotter))
        action3.triggered.connect(lambda: ssao_shader(self.plotter_widget.plotter))
    
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName()
        #file_dialog = QFileDialog(self)
        #file_dialog.exec()

        #selected_file = file_dialog.selectedFiles()[0]
        selected_file = file_path
        file_handling.read_file(selected_file,self.plotter_widget.plotter)

    def create_toolbar(self):
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        # Add the buttons with icons to the toolbar
        toolbar.addAction(QIcon("top_view_icon.png"), "Top View")
        toolbar.addAction(QIcon("bottom_view_icon.png"), "Bottom View")
        toolbar.addAction(QIcon("left_side_view_icon.png"), "Left Side View")
        toolbar.addAction(QIcon("right_side_view_icon.png"), "Right Side View")
        toolbar.addAction(QIcon("gui/static/front-view.png"), "Front View",lambda: front_view(self.plotter_widget.plotter))
        toolbar.addAction(QIcon("back_view_icon.png"), "Back View")
        toolbar.addAction(QIcon("front_isometric_icon.png"), "Front Isometric")
        toolbar.addAction(QIcon("back_isometric_icon.png"), "Back Isometric")
'''