import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLabel, QDialog, QFileDialog, QLineEdit
from krita import DockWidget
from .addcomponent import AddComponent

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

        # Create a button to add boxes
        self.addButton = QPushButton('Add Box', self)
        self.addButton.clicked.connect(self.addBox)
        self.main_layout.addWidget(self.addButton)

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
        options = QFileDialog.Options()
        folderPath = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)
        if folderPath:
            print("Selected Folder:", folderPath)

    def addBox(self):
        box = AddComponent()
        # insert the box before the Add Box button and stretchable space
        self.main_layout.insertWidget(self.main_layout.count() - 2, box)
        box.deleteButton.clicked.connect(lambda: self.deleteBox(box))

    def deleteBox(self, box):
        box.setParent(None)
        box.deleteLater()

    # 'pass' means do not do anything
    def canvasChanged(self, canvas):
        pass