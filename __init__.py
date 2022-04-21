

import os

bl_info = {
    "name": "bitto",
    "author": "Joey Chen",
    "version": (1, 0, 1),
    "blender": (3, 0, 0),
    "location": "",
    "description": "Renderer Addon Template",
    "warning": "",
    "category": "Render"
}

if "bpy" in locals():
    import importlib
    importlib.reload(ui)
else:
    import bpy


def register():
    print('registering the xxx renderer')
    pass


def unregister():
    pass


if __name__ == '__main__':
    register()