from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox, QWidget, QFrame, QCheckBox, QListWidgetItem, QDialog


class AddComponent(QWidget):
    def __init__(self):
        super().__init__()
        self.layout_panel = QVBoxLayout(self)

        self.materialPanel()

    def materialPanel(self):
        # Function Call
        self.texture_basic_info()
        self.texture_map_info()
        self.texture_normal_info()

        self.deleteButton = QPushButton('Delete', self)
        self.layout_panel.addWidget(self.deleteButton)
    
    def texture_basic_info(self):
        self.layout_texture_basic_info = QHBoxLayout()

        self.titleLabel = QLabel('Sufix:', self)
        self.layout_texture_basic_info.addWidget(self.titleLabel)

        self.line_edit_sufix = QLineEdit()  # Create a QLineEdit widget
        self.layout_texture_basic_info.addWidget(self.line_edit_sufix)

        self.layout_panel.addLayout(self.layout_texture_basic_info)

        # Image Format
        self.combo_box_format = QComboBox()
        self.combo_box_format.addItems(['TGA', 'PNG', 'JPG', 'TIFF', 'PSD'])
        self.combo_box_format.currentIndexChanged.connect(self.comboBoxChanged)
        self.layout_texture_basic_info.addWidget(self.combo_box_format)

        # Image Scale
        self.combo_box_scale = QComboBox()
        self.combo_box_scale.addItems(['200%', '100%', '50%', '25%', '12,5%'])
        self.combo_box_scale.setCurrentIndex(1)
        self.combo_box_scale.currentIndexChanged.connect(self.comboBoxChanged)
        self.layout_texture_basic_info.addWidget(self.combo_box_scale)
    
    def texture_map_info(self):
        self.layout_texture_map_info = QHBoxLayout()

        self.titleLabel = QLabel('Texture Map:', self)
        self.layout_texture_map_info.addWidget(self.titleLabel)

        # Map Type
        self.map_types_list = ['None', 'Color', 'Normal', 'Roughness', 'Metallic', 'Ambient Occlusion', 'Height', 'Mask', 'Emissive']
        self.combo_box_map_type = QComboBox()
        self.combo_box_map_type.setCurrentIndex(0)
        
        self.combo_box_map_type.currentIndexChanged.connect(self.comboBoxChanged)
        self.layout_texture_map_info.addWidget(self.combo_box_map_type)

        # Alpha channel
        self.titleLabel_alpha = QLabel('Alpha:', self)
        self.checkbox_alpha = QCheckBox()
        self.layout_texture_map_info.addWidget(self.titleLabel_alpha)
        self.layout_texture_map_info.addWidget(self.checkbox_alpha)
        self.alpha_toggle(False)

        self.checkbox_alpha.stateChanged.connect(self.alpha_toggle)

        self.layout_panel.addLayout(self.layout_texture_map_info)
    
    def comboBoxChanged(self):
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
            self.map_types_list_alpha = [item for item in self.map_types_list if item not in ['None', 'Color', 'Normal']]
            self.combo_box_map_type.addItems(self.map_types_list_alpha)
        else:
            self.combo_box_map_type.clear() # Clear itens
            self.combo_box_map_type.addItems(self.map_types_list)




