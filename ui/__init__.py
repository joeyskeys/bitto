from . import film
from . import camera


def register():
    film.register()
    camera.register()


def unregister():
    film.unregister()
    camera.unregister()