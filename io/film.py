
import bpy
import mathutils


class FilmIO(object):
    """
    """

    def __init__(self):
        for prop in config.camera_props:
            prop['type']

    def get_resolution(self):
        render = bpy.context.scene.render
        return (render.resolution_x, render.resolution_y)

    def get_props(self):
        active_cam = bpy.context.scene.camera
        return active_cam.data.bitto_camera_props
