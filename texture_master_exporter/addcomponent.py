from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox, QWidget, QFrame, QCheckBox, QListWidgetItem


class AddComponent(QWidget):
    def __init__(self):
        super().__init__()
        self.materialPanel()

    def materialPanel(self):
        self.layout = QVBoxLayout(self)

        self.titleLabel = QLabel('Title', self)
        self.layout.addWidget(self.titleLabel)

        self.deleteButton = QPushButton('Delete', self)
        self.layout.addWidget(self.deleteButton)