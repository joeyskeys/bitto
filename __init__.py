import os
import config

bl_info = {
    "name": config.name,
    "author": config.author,
    "version": config.version,
    "blender": config.blender_version,
    "location": config.location,
    "description": config.description,
    "warning": config.warning,
    "category": "Render"
}

if "bpy" in locals():
    import importlib
    importlib.reload(ui)
else:
    import bpy


def register():
    print('registering the xxx renderer')
    from utils.registry import regular_registry, shading_node_registry

    regular_registry.register()
    shading_node_registry.register()


def unregister():
    from utils.registry import regular_registry, shading_node_registry

    regular_registry.unregister()
    shading_node_registry.unregister()


if __name__ == '__main__':
    register()