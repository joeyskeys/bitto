
from pydoc import render_doc
import bpy
from .base import BittoProperties, setup_ui
from ..utils.registry import regular_registry, property_group_registry


class BittoLightProperty(BittoProperties):
    pass

BittoLightProperty.init_annotations(config.light_props)


class Bitto_PT_light(bpy.types.Panel):
    bl_label = "Light"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    COMPAT_ENGINES = {config.engine_name}
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        renderer = context.scene.render
        return render.engine == config.engine_name and context.active_object.type == 'LIGHT'

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        light = context.active_object.data


regular_registry.add_new_class(Bitto_PT_light)
property_group_registry.add_new_property_class(BittoLightProperty, "bitto_light_props")