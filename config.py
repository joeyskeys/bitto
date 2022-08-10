
engine_name = "EXAMPLE_RENDER"
engine_label = "Example"

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

camera_props = ()

integrator_props = ()

light_props = ()

sampler_props = ()

world_props = ()

preference_props = ()

node_categories = (
    ('BITTO_MATERIAL', 'Material'),
    ('BITTO_TEXTURE', 'Texture'),
)