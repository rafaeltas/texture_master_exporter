import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLabel, QDialog, QFileDialog, QLineEdit, QSizePolicy
from PyQt5.QtCore import Qt, QTimer
from krita import DockWidget
from .addcomponent import AddComponent
from .exporter import ExportLayers
from .textures_data import texture_map_data, path_folder

DOCKER_TITLE = 'Exporter Texture Master'


class exporterTextureMaster(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_TITLE)
        self.initUI()

    def initUI(self):
        widget = QWidget(self)  # Create a central widget
        self.setWidget(widget) 

        self.main_layout = QVBoxLayout(widget)

        #calls
        self.block_folder_path()

        # Create a button to add texture boxes
        self.v_layout_texture_boxes = QVBoxLayout()
        self.main_layout.addLayout(self.v_layout_texture_boxes)        
        self.addButton = QPushButton('Add Box', self)
        self.addButton.clicked.connect(self.addBox)
        self.v_layout_texture_boxes.addWidget(self.addButton)

        self.exportButton = QPushButton('Export', self)
        
        self.exportButton.clicked.connect(self.export_maps)
        self.main_layout.addWidget(self.exportButton)
        
        # self.frame = QFrame()
        # self.frame.setFrameShape(QFrame.StyledPanel)
        # self.frame.setFrameShadow(QFrame.Raised)
        # self.frame.setStyleSheet("background-color: lightblue;")
        # self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.layout_delete_button.addWidget(self.frame)
        
        
        self.adjustSize() #Scyn size of Docker by content


    def block_folder_path(self):
        # Select Path to export files.
        app = Krita.instance()
        self.h_layout_folder_path = QHBoxLayout()

        self.line_edit_path = QLineEdit()  # Create a QLineEdit widget

        self.button_folder = QPushButton('Select Folder', self)
        self.button_folder.setIcon(app.icon('folder'))
        self.button_folder.clicked.connect(self.selectFolder)

        # Layout
        self.h_layout_folder_path.addWidget(self.line_edit_path)
        self.h_layout_folder_path.addWidget(self.button_folder)
        self.main_layout.addLayout(self.h_layout_folder_path)


    def selectFolder(self):
        self.path_folder = path_folder
        options = QFileDialog.Options()
        folderPath = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)
        if folderPath:
            self.line_edit_path.setText(folderPath)
            self.path_folder.append(self.line_edit_path.text())
            

    def addBox(self):
        box = AddComponent()
        texture_map_position = self.v_layout_texture_boxes.count() - 1
        self.v_layout_texture_boxes.insertWidget(self.v_layout_texture_boxes.count() - 1, box)
        
        box.deleteButton.clicked.connect(lambda: self.deleteBox(box))
        self.adjustSize() #Scyn size of Docker by content

    def deleteBox(self,box):
        box.setParent(None)
        box.deleteLater()
        self.id_target = box.id_texture
        del texture_map_data[f"{self.id_target}"]
        self.adjustSize()  # Sync size of Docker by content
        self.main_layout.addStretch()  # Get content to the top.

    # Export maps function
    def export_maps(self):
        export_process = ExportLayers
        export_process()

    # 'pass' means do not do anything
    def canvasChanged(self, canvas):
        pass