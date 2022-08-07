
name = "bitto"
author = "Joey Chen"
version = (1, 0, 0)
blender_version = (3, 0, 0)
location = ""
description = "Blender Addon Template for Renderers"
warning = ""

engine_name = "EXAMPLE_RENDER"

camera_props = (
    {
        'type' : 'float',
        'props' : {
            'name' : 'example',
            'description' : 'this is a example property',
            'default' : 0,
            'min' : 0,
            'max' : 1
        }
    },
    {
        'type' : 'string',
        'props' : {
            'name' : 'string_prop',
            'description' : 'this is a example float property',
            'default' : '',
            'subtype' : 'FILE_PATH'
        }
    }
)