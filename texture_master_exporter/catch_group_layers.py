from krita import Krita

app = Krita.instance()
currentDoc = app.activeDocument()
topLevelLayers = currentDoc.topLevelNodes()

# Texture Maps Orders
texture_map = ["Normal"]

 # Compare lists
lib_toplayers = []
for layers in topLevelLayers:    
    lib_toplayers.append(layers.name())    

    export_list = [image_export for image_export in texture_map if image_export in lib_toplayers]
    
    if layers.name() not in export_list:
        layers.setVisible(False) #Control visibility
        currentDoc.refreshProjection() # Refresh viewport to give feedback on screen
