from PyQt5.QtWidgets import QDialog, QHBoxLayout, QPushButton, QLabel
from krita import Krita, InfoObject
from .textures_data import texture_map_data, path_folder
import os

app = Krita.instance()  
doc = app.activeDocument()

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
            self.exportParameters = InfoObject()
            self.exportParameters.setProperty("alpha", True)
            self.exportParameters.setProperty("compression", 6)  
            self.exportParameters.setProperty("indexed", False)
            currentDocument.setBatchmode(False) # Change further
            
            for key, value in texture_map_data.items():             
               
                image_sufix = texture_map_data[f"{key}"]["line_edit_sufix"]
                image_format = texture_map_data[f"{key}"]["combobox_format"]
                image_scale = texture_map_data[f"{key}"]["combobox_scale"]
                image_type = texture_map_data[f"{key}"]["combobox_type"]
                image_alpha = texture_map_data[f"{key}"]["checkbox_alpha"] # Boolean
                
                image_name = self.image_naming(str(image_sufix), str(image_type))
                
# exportImage
                self.filter_by_groups_names(image_type)
                currentDocument.exportImage(f'{self.path_folder[0]}/{image_name}.{image_format}', self.exportParameters )
                
                topLevelLayers = currentDocument.topLevelNodes()    
                for layers in topLevelLayers:    
                    layers.setVisible(True) #Control visibility
                    currentDocument.refreshProjection() # Refresh viewport to give feedback on screen
                        
    def image_naming(self, sufix, type):        
# Set default name is the current file name
        if sufix and type == "None":            
            file_path = Krita.instance().activeDocument().fileName()
            default_name = file_path.split('/')[-1]
            return f"{default_name}"
        
        if sufix and type != "None":
            final_name = f"{sufix}_{type}"
            return final_name
        
        if sufix =="None" and type != "None":
            return (None, f"{type}")


# Filter all groupNodes(Top Group Layer)
    def filter_by_groups_names(self, texturemap):
        app = Krita.instance()
        currentDoc = app.activeDocument()
        topLevelLayers = currentDoc.topLevelNodes()
    # Texture Maps Orders
        texture_map = [f"{texturemap}"]
    # Compare lists
        lib_toplayers = []
        for layers in topLevelLayers:    
            lib_toplayers.append(layers.name())
            export_list = [image_export for image_export in texture_map if image_export in lib_toplayers]
            
            if layers.name() not in export_list:
                layers.setVisible(False) #Control visibility
                currentDoc.refreshProjection() # Refresh viewport to give feedback on screen

            
# DEBUG!!
    def _debug_function(self):
        layoutForButtons = QHBoxLayout()
        data_as_string = str(texture_map_data)
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