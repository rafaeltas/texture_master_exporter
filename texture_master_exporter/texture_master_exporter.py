from PyQt5.QtWidgets import QWidget, QPushButton, QDialog, QLabel, QCheckBox, QVBoxLayout, QHBoxLayout, QLineEdit, QFileDialog, QGroupBox
from krita import DockWidget

DOCKER_TITLE = 'Blank Template Docker'

class DockerTemplate(DockWidget):

    def __init__(self):
        super().__init__()
        self.mainExporter()

    def mainExporter(self):
        self.layout_exporter = QVBoxLayout(self)

        self.titleLabel = QLabel('Testing Docker', self)
        self.layout_exporter.addWidget(self.titleLabel)

        self.content_test = QLabel('Delete', self)
        self.layout_exporter.addWidget(self.content_test)

    # 'pass' means do not do anything
    def canvasChanged(self, canvas):
        pass
