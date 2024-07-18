from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox, QWidget, QFrame, QCheckBox, QListWidgetItem, QDialog


class AddComponent(QWidget):
    def __init__(self):
        super().__init__()

        # newDialog = QDialog()
        # newDialog.setWindowTitle("new Dialog Title!")
        # newDialog.exec_()

        self.materialPanel()

    def materialPanel(self):
        self.layout = QVBoxLayout(self)

        self.titleLabel = QLabel('Title', self)
        self.layout.addWidget(self.titleLabel)

        self.deleteButton = QPushButton('Delete', self)
        self.layout.addWidget(self.deleteButton)