
name = "bitto"
author = "Joey Chen"
version = (1, 0, 0)
blender_version = (3, 0, 0)
location = ""
description = "Blender Addon Template for Renderers"
warning = ""

engine_name = "EXAMPLE_RENDER"

film_props = (
    {
        'type' : 'float',
        'name' : 'example',
        'text' : 'Example',
        'props' : {
            'description' : 'this is a example property',
            'default' : 0,
            'min' : 0,
            'max' : 1
        }
    },
    {
        'type' : 'string',
        'name' : 'string_prop',
        'text' : 'BlaBla',
        'props' : {
            'description' : 'this is a example float property',
            'default' : '',
            'subtype' : 'FILE_PATH'
        }
    }
)

camera_props = (
    
)