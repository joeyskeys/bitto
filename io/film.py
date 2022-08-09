
import bpy
import mathutils


class FilmIO(object):
    """
    """

    def __init__(self):
        pass

    def get_resolution(self):
        render = bpy.context.scene.render
        return (render.resolution_x, render.resolution_y)

    def get_props(self):
        return bpy.context.scene.bitto_film_props
