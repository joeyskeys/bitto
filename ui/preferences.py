
import os
import bpy
from .. import config
from .base import init_annotations, setup_ui
from ..utils.registry import regular_registry


addon_name = config.engine_label


class BittoPreferences(bpy.types.AddonPreferences):
    bl_idname = addon_name

    def draw(self, context):
        layout = self.layout
        setup_ui(layout, config.preference_props, self)

init_annotations(BittoPreferences, config.preference_props)


def get_pref():
    return bpy.context.preferences.addons[addon_name].preferences


def setup():
    regular_registry.add_new_class(BittoPreferences)