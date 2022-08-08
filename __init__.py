import os
from . import config


# Sadly bl_info related fields cannot be put into config or it will coz an 
# ast parse traceback
bl_info = {
    "name": "bitto",
    "author": "Joey Chen",
    "version": (0, 0, 1),
    "blender": (3, 2, 0),
    "location": "",
    "description": "Blender Addon Template for Renderers",
    "warning": "",
    "category": "Render"
}

if "bpy" in locals():
    import importlib
    importlib.reload(ui)
else:
    import bpy


def register():
    print('registering the {} renderer'.format(config.engine_name))
    from .utils.registry import regular_registry, shading_node_registry
    from . import render
    from . import ui

    regular_registry.register()
    shading_node_registry.register()
    render.register()
    ui.register()


def unregister():
    from .utils.registry import regular_registry, shading_node_registry
    from . import render
    from . import ui

    regular_registry.unregister()
    shading_node_registry.unregister()
    render.unregister()
    ui.unregister()


if __name__ == '__main__':
    register()