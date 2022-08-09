

import bpy
from .. import config
from .base import BittoProperties, setup_ui
from ..utils.registry import regular_registry, property_group_registry


class BittoFilmProperties(BittoProperties):
    pass

BittoFilmProperties.init_annotations(config.film_props)


class Bitto_PT_film(bpy.types.Panel):
    bl_label = "Film"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    COMPAT_ENGINES = {config.engine_name}
    bl_context = "output"

    @classmethod
    def poll(cls, context):
        render = context.scene.render
        return render.engine == config.engine_name

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        render = context.scene.render
        layout.row().prop(render, "resolution_x", text="Resolution X")
        layout.row().prop(render, "resolution_y", text="Resolution Y")

        film_props = context.scene.bitto_film_props
        setup_ui(layout, config.film_props, film_props)


'''
def register():
    # Register property group
    bpy.utils.register_class(BittoFilmProperties)
    bpy.types.Scene.bitto_film_props = bpy.props.PointerProperty(type=BittoFilmProperties)

    # Register UIs
    bpy.utils.register_class(Bitto_PT_film)


def unregister():
    # Unregister property group
    del bpy.types.Scene.bitto_film_props
    bpy.utils.unregister_class(BittoFilmProperties)

    # Unregister UIs
    bpy.utils.unregister_class(Bitto_PT_film)
'''

def setup():
    regular_registry.add_new_class(Bitto_PT_film)
    property_group_registry.add_new_property_class(BittoFilmProperties, bpy.types.Scene, "bitto_film_props")