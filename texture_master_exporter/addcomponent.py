from PyQt5.QtWidgets import QApplication, QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox, QWidget, QFrame, QCheckBox, QListWidgetItem, QDialog
from PyQt5.QtCore import Qt
from .textures_data import texture_map_data
import random
import string


class AddComponent(QWidget):
    
    
    def __init__(self):
        super().__init__()
        self.layout_panel = QVBoxLayout(self)
        self.id_texture = {}
        self.data_teste = texture_map_data
        self.random_ids()
        self.materialPanel()
        
        
    def materialPanel(self):

        app = Krita.instance()
        self.layout_delete_button = QHBoxLayout()
        self.layout_delete_button.setAlignment(Qt.AlignRight)
        
        # self.layout_delete_button.addStretch() # Align button to right side.
        self.deleteButton = QPushButton() #'Delete' Button
        self.deleteButton.setIcon(app.icon('deletelayer'))
        self.deleteButton.setFixedSize(self.deleteButton.sizeHint()) #Fit size of button by size of Icon.
        self.layout_delete_button.addWidget(self.deleteButton)
        self.layout_panel.addLayout(self.layout_delete_button)

        # Function Call
        self.texture_basic_info()
        self.texture_map_info()
        self.texture_normal_info()

        self.layout_panel.addStretch() # Get content to the top.

    
    def random_ids(self):
        letra = random.choice(string.ascii_uppercase)
        numeros = random.randint(0, 999)
        self.nova_id = f"{letra}{numeros:03}"
            
        if self.nova_id not in self.data_teste:
            self.id_texture = f"{self.nova_id}"
            self.data_teste[f"{self.nova_id}"] = {"line_edit_sufix":"None",
                                                  "combobox_format":"PNG",
                                                  "combobox_scale":"100%",
                                                  "combobox_type":"None",
                                                  "checkbox_alpha":False                                            
                                                  } # Data pattern
            return self.id_texture
        else:
            self.random_ids()
    
    def texture_basic_info(self):
        self.layout_texture_basic_info = QHBoxLayout()

        self.titleLabel = QLabel('Sufix:', self)
        self.layout_texture_basic_info.addWidget(self.titleLabel)

        self.line_edit_sufix = QLineEdit()  # Create a QLineEdit widget
        self.layout_texture_basic_info.addWidget(self.line_edit_sufix)

        self.layout_panel.addLayout(self.layout_texture_basic_info)

        # Image Format
        self.combo_box_format = QComboBox()
        self.combo_box_format_list = ['TGA', 'PNG', 'JPG', 'TIFF', 'PSD']
        self.combo_box_format.addItems(self.combo_box_format_list)
        self.combo_box_format.setCurrentIndex(1)
        
        self.combo_box_format.currentIndexChanged.connect(self.combo_box_changed)
        self.layout_texture_basic_info.addWidget(self.combo_box_format)
        

        # Image Scale
        self.combo_box_scale = QComboBox()
        self.combo_box_scale_list = ['200%', '100%', '50%', '25%', '12,5%']
        self.combo_box_scale.addItems(self.combo_box_scale_list)
        self.combo_box_scale.setCurrentIndex(1)
        
        self.combo_box_scale.currentIndexChanged.connect(self.combo_box_changed)
        self.layout_texture_basic_info.addWidget(self.combo_box_scale)
        # self.data_teste[f"{self.nova_id}"] = {"combobox_scale":"100%"}
    
    def texture_map_info(self):
        self.layout_texture_map_info = QHBoxLayout()

        self.titleLabel = QLabel('Texture Map:', self)
        self.layout_texture_map_info.addWidget(self.titleLabel)

        # Map Type
        self.combo_box_map_type_list = ['None', 'Color', 'Normal', 'Roughness', 'Metallic', 'Ambient Occlusion', 'Height', 'Mask', 'Emissive']
        self.combo_box_map_type = QComboBox()
        self.combo_box_map_type.setCurrentIndex(0)
        
        self.combo_box_map_type.currentIndexChanged.connect(self.combo_box_changed)
        self.layout_texture_map_info.addWidget(self.combo_box_map_type)

        # Alpha channel
        self.titleLabel_alpha = QLabel('Alpha:', self)
        self.checkbox_alpha = QCheckBox()
        self.layout_texture_map_info.addWidget(self.titleLabel_alpha)
        self.layout_texture_map_info.addWidget(self.checkbox_alpha)
        self.alpha_toggle(False)

        self.checkbox_alpha.stateChanged.connect(self.alpha_toggle)

        self.layout_panel.addLayout(self.layout_texture_map_info)
    
    
    
    def combo_box_changed(self,value):#, key, value
        
        # Verify ID Texture individual and in textures data
        if self.id_texture in self.data_teste:
            if self.combo_box_format.currentText() in self.combo_box_format_list:
                self.data_teste[f"{self.id_texture}"]["combobox_format"] = f"{self.combo_box_format.currentText()}"
            # self.combo_box_format_list
            # self.combo_box_scale_list
            # self.combo_box_map_type_list
            
        
        # Put the new "key" and new "value" in textures data
        
        
        # self.changed_option = self.combo_box_map_type.currentText()
        # single_texture_map_data[f"{self.single_texture_map_data}"] = {"texture_name":f"{self.changed_option}"}
        pass
    
    def check_box_Changed(self):#, key, value
        # self.changed_option = self.combo_box_map_type.currentText()
        # single_texture_map_data[f"{self.single_texture_map_data}"] = {"texture_name":f"{self.changed_option}"}
        pass
        
        

    def texture_normal_info(self):
        self.layout_texture_normal_info = QHBoxLayout()

        self.titleLabel_normal = QLabel('Normals:', self)
        self.layout_texture_normal_info.addWidget(self.titleLabel_normal)

        self.titleLabel_normal_flip_x = QLabel('Flip X:', self)
        self.layout_texture_normal_info.addWidget(self.titleLabel_normal_flip_x)

        self.titleLabel_normal_flip_y = QLabel('Flip Y:', self)
        self.layout_texture_normal_info.addWidget(self.titleLabel_normal_flip_y)

        self.layout_panel.addLayout(self.layout_texture_normal_info)

    def alpha_toggle(self, state):
        if self.checkbox_alpha.isChecked() is True:
             # Remove specific items
            self.combo_box_map_type.clear() # Clear itens
            self.map_types_list_alpha = [item for item in self.combo_box_map_type_list if item not in ['None', 'Color', 'Normal']]
            self.combo_box_map_type.addItems(self.map_types_list_alpha)
        else:
            self.combo_box_map_type.clear() # Clear itens
            self.combo_box_map_type.addItems(self.combo_box_map_type_list)





