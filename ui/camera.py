
import bpy


class BittoCameraProperties(BittoProperties):
    def __init__(self):
        super(BittoCameraProperties, self).__init__(config.camera_props)


class Bitto_PT_camera(bpy.types.Panel):
    bl_label = "Camera"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    COMPAT_ENGINES = {config.engine_name}
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        renderer = context.scene.render
        return renderer.engine == 'PBRT_RENDER' and context.active_object.type == 'CAMERA'

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        camera_props = context.scene.bitto_camera_props
        setup_ui(layout, config.camera_props, camera_props)


def register():
    # Register property group
    bpy.utils.register_class(BittoCameraProperties)
    bpy.types.Scene.bitto_film_props = bpy.props.PointerProperty(type=BittoCameraProperties)

    # Register UIs
    bpy.utils.register_class(Bitto_PT_camera)


def unregister():
    # Unregister property group
    del bpy.types.Scene.bitto_camera_props
    bpy.utils.unregister_class(BittoCameraProperties)

    # Unregister UIs
    bpy.utils.unregister_class(Bitto_PT_camera)