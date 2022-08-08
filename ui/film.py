

import bpy
from .. import config
from .base import BittoProperties, setup_ui, static_init


class BittoFilmProperties(BittoProperties):
    pass


print('static init film props')
BittoFilmProperties.static_init(config.film_props)
print(dir(BittoFilmProperties))


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