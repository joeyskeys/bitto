import bpy
from ..utils.typemap import bprop_map


def static_init(cls, prop_dict):
    if getattr(cls, 'static_init', None) and not getattr(cls, prop_dict[0]['name'], None):
        cls.static_init(prop_dict)
    return cls


class BittoProperties(bpy.types.PropertyGroup):
    @classmethod
    def static_init(cls, prop_dict):
        print('static init for ', cls.__name__)
        for attr in prop_dict:
            bprop = bprop_map[attr['type']](**attr['props'])
            print('setting {} to {}'.format(bprop, attr['name']))
            setattr(cls, attr['name'], bprop)


def setup_ui(layout, prop_dict, prop):
    for attr in prop_dict:
        layout.row().prop(prop, attr['name'], text=attr['text'])


def register_ui(prop_name, prop_class, ui_class):
    # Register property group
    bpy.utils.register_class(prop_class)
    pt = bpy.props.PointerProperty(type=prop_class)
    setattr(bpy.typs.Scene, prop_name, pt)

    # Register UIs
    bpy.utils.register_class(ui_class)


def unregister_ui(prop_name, prop_class, ui_class):
    # Unregister property group
    delattr(bpy.types.Scene, prop_name)
    bpy.utils.unregister_class(prop_class)

    # Unregister UIs
    bpy.utils.unregister_class(ui_class)