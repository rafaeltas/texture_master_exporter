from PyQt5.QtWidgets import QDialog, QHBoxLayout, QPushButton, QLabel
from krita import Krita, InfoObject
from .textures_data import texture_map_data, path_folder
import os

app = Krita.instance()  
doc = app.activeDocument()
    #     group_names = []
    #     if node and node.childNodes():
    #         for child in node.childNodes():
    #             if child.type() == 'grouplayer':
    #                 group_names.append(child.name())
    #                 group_names.extend(get_group_layer_names(child))
    #     return group_names

    # if doc:
    #     root = doc.rootNode()
    #     group_names = get_group_layer_names(root)
    #     print("Group layer names:", group_names)
    # else:
    #     print("No document is currently open.")

class ExportLayers():

    def __init__(self):
        self.group_layers_names = []
        self.catch_name_texture_map()
        self.set_export_settings()
        self._debug_function()

    def catch_name_texture_map(self):
        # Catch layergroup by name
        doc = Krita.instance().activeDocument()
        if not doc:
            print("Has no layer group with this texture map.")
            return

        root = doc.rootNode()
        for node in root.childNodes():
            if node.type() == 'grouplayer':
                self.group_layers_names.append(f"{node.name()}")
                print(node.name())
        
    def set_export_settings(self):

        self.path_folder = path_folder
        if len(texture_map_data) == 0 or len(self.path_folder) == 0:
            self.layout_texture_map_alert = QHBoxLayout()
            self.layout_texture_map_alert_label = QLabel("Has no any textures to export,<br>or has no set path to save the files.")
            self.layout_texture_map_alert.addWidget(self.layout_texture_map_alert_label)
            # Set dialog
            newDialog = QDialog()
            newDialog.setLayout(self.layout_texture_map_alert)
            newDialog.setWindowTitle("Alert!")
            newDialog.setStyleSheet("min-width:300px")
            newDialog.exec_()
        else:
            currentDocument = Krita.instance().activeDocument()

            # setup some export parameters
            exportParameters = InfoObject()
            exportParameters.setProperty("alpha", True)
            exportParameters.setProperty("compression", 6)  
            exportParameters.setProperty("indexed", False)
            currentDocument.setBatchmode(False) # Change further

            # exportImage supports jpg and png
            currentDocument.exportImage(f'{self.path_folder[0]}/export-image.png', exportParameters )
        
        
    # DEBUG!!
    def _debug_function(self):
        layoutForButtons = QHBoxLayout()
        data_as_string = str(path_folder)
        # newButton = QPushButton(f"Name Map is {data_as_string}")
        newButton = QPushButton(f"Name Map is {data_as_string}")
    
        newButton.setIcon(app.icon('animation_play'))
        #newButton = QPushButton("Press me")
        layoutForButtons.addWidget(newButton)

        #create dialog and show it
        newDialog = QDialog()
        newDialog.setLayout(layoutForButtons)
        newDialog.setWindowTitle("new Dialog Title!")
        newDialog.exec_()