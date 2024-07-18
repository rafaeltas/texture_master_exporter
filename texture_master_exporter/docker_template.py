from krita import DockWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox
import sys

DOCKER_TITLE = 'Exporter Docker'

class DockerTemplate(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_TITLE)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('ComboBox Example')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout(self)

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Option 1")
        self.comboBox.addItem("Option 2")
        self.comboBox.addItem("Option 3")
        self.comboBox.currentIndexChanged.connect(self.comboBoxChanged)

        layout.addWidget(self.comboBox)

    def comboBoxChanged(self, index):
        selected_option = self.comboBox.currentText()
        print("Selected option:", selected_option)


    # notifies when views are added or removed
    # 'pass' means do not do anything
    def canvasChanged(self, canvas):
        pass


