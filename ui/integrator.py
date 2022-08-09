
import bpy
from .base import BittoProperties, setup_ui
from ..utils.registry import regular_registry, property_group_registry


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
        layout = self.layout
        layout.use_property_split = True


regular_registry.add_new_class(Bitto_PT_integrator)
property_group_registry.add_new_property_class(BittoIntegratorProperties, "bitto_integrator_props")