from PyQt5.QtWidgets import QMenuBar, QAction, QFileDialog
from PyQt5.QtGui import QIcon
from data_io import file_handling
from data_visualization.filters import edl_shader,remove_filter, ssao_shader

def create_menu_bar(main_window):
    menu_bar = QMenuBar(main_window)
    main_window.setMenuBar(menu_bar)

    #Create File Menu
    file_menu = menu_bar.addMenu("File")
    #Create Open Option
    open_action = QAction(QIcon("gui/static/open-folder.png"), "Open", file_menu)
    open_action.triggered.connect(lambda: file_dialog(main_window))
    file_menu.addAction(open_action)

    #Create Display Menu
    display_menu = menu_bar.addMenu("Display")
    #Create Shaders & Filters Option
    shader_filters_menu = display_menu.addMenu("Shader && Filters")
    shader_filters_menu.setIcon(QIcon("gui/static/shader.png"))

    #Add Sub Menu
    action1 = QAction("Remove Filters " ,main_window)
    action2 = QAction("EDL Shader"      ,main_window)
    action3 = QAction("SSAO Shader"     ,main_window)

    shader_filters_menu.addAction(action1)
    shader_filters_menu.addAction(action2)
    shader_filters_menu.addAction(action3)

    action1.triggered.connect(lambda: remove_filter(main_window.plotter_widget.plotter))
    action2.triggered.connect(lambda: edl_shader(main_window.plotter_widget.plotter))
    action3.triggered.connect(lambda: ssao_shader(main_window.plotter_widget.plotter))


    #Add BOunding Axes

# Function for open action in File
def file_dialog(main_window):
    selected_file, _ = QFileDialog.getOpenFileName()
    file_handling.read_file(selected_file, main_window.plotter_widget.plotter)





