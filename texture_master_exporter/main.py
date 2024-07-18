import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QDialog, QLabel, QCheckBox, QVBoxLayout, QHBoxLayout, QLineEdit, QFileDialog, QGroupBox
from krita import DockWidget
from .addcomponent import AddComponent

DOCKER_TITLE = 'Exporter Texture Master'


class exporterTextureMaster(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_TITLE)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        # Add a stretchable space to push boxes to the bottom
        self.layout.addStretch()

        # Create a button to add boxes
        self.addButton = QPushButton('Add Box', self)
        self.addButton.clicked.connect(self.addBox)
        self.layout.addWidget(self.addButton)

    def addBox(self):
        box = AddComponent()
        # insert the box before the Add Box button and stretchable space
        self.layout.insertWidget(self.layout.count() - 2, box)
        box.deleteButton.clicked.connect(lambda: self.deleteBox(box))

    def deleteBox(self, box):
        box.setParent(None)
        box.deleteLater()

    # 'pass' means do not do anything
    def canvasChanged(self, canvas):
        pass