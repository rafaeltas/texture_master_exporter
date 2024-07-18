from krita import DockWidgetFactory, DockWidgetFactoryBase
from .main import exporterTextureMaster

DOCKER_ID = 'texture_master_exporter_docker'
instance = Krita.instance()
dock_widget_factory = DockWidgetFactory(DOCKER_ID,
                                        DockWidgetFactoryBase.DockRight,
                                        exporterTextureMaster)

instance.addDockWidgetFactory(dock_widget_factory)