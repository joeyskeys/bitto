
import bpy
from .base import BaseIO


class AcceleratorIO(BaseIO):
    """
    """

    def __init__(self):
        pass

    def get_props(self):
        return bpy.context.scene.bitto_accelerator_props

    def write_description(self, writer):
        pass

    def read_description(self, reader):
        pass

    def feed_api(self):
        pass