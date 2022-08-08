
import bpy
from ui.base import BittoProperties


class BittoIntegratorProperties(BittoProperties):
    pass

BittoIntegratorProperties.init_annotations(config.integrator_props)


class Bitto_PT_integrator(bpy.types.Panel):
    bl_label = "Integrator"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    COMPAT_ENGINES = {config.engine_name}
    bl_context = "render"

    @classmethod
    def poll(cls, context):
        render = context.scene.render
        return render.engine == config.engine_name

    def draw(self, context):
        pass