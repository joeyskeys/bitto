
import os
import bpy
import time
from .. import config
from ..utils.registry import regular_registry


class BittoRenderEngine(bpy.types.RenderEngine):
    bl_idname = config.engine_name
    bl_label = config.engine_label
    bl_use_preview = True
    bl_use_shading_nodes = False
    bl_use_postprocess = True

    # Ctor
    def __init__(self):
        self.renderer = None

    def __del__(self):
        pass

    def render(self, depsgraph):
        print("Currently just print 'rendering'")

    def view_update(self, context, depsgraph):
        pass

    def view_draw(self, context, depsgraph):
        pass


def setup():
    regular_registry.add_new_class(BittoRenderEngine)