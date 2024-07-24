from PyQt5.QtWidgets import QDialog, QHBoxLayout, QPushButton
from krita import Krita
from .textures_data import texture_map_data

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
        self.catch_name_texture_map()
        self._debug_function()

    def catch_name_texture_map(self):
        pass
    
    def _debug_function(self):

        layoutForButtons = QHBoxLayout()
        data_as_string = str(texture_map_data)
        newButton = QPushButton(f"Name Map is {data_as_string}") 
        # newButton = QPushButton(f"Name Map is {texture_map_data}")
        newButton.setIcon(app.icon('animation_play'))
        #newButton = QPushButton("Press me")
        layoutForButtons.addWidget(newButton)

        #create dialog and show it
        newDialog = QDialog()
        newDialog.setLayout(layoutForButtons)
        newDialog.setWindowTitle("new Dialog Title!")
        newDialog.exec_()