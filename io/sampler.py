
import bpy
from .base import BaseIO


class SamplerIO(BaseIO):
    def __init__(self):
        pass

    def get_props(self):
        return bpy.context.scene.bitto_sampler_props