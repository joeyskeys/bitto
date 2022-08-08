import bpy


class Registry(object):
    def __init__(self):
        self.cls_to_register = []

    def add_new_class(self, cls):
        self.cls_to_register.append(cls)

    def register(self):
        for c in self.cls_to_register:
            print('register', c)
            bpy.utils.register_class(c)

    def unregister(self):
        for c in self.cls_to_register:
            bpy.utils.unregister_class(c)


class ShadingNodeRegistry(Registry):
    def __init__(self):
        super(ShadingNodeRegistry, self).__init__()
        self.material_nodes = []
        self.texture_nodes = []

    def add_new_shading_class(self, cls, node_type=None):
        self.add_new_class(cls)

        if node_type == 'material':
            self.material_nodes.append((cls.class_type, cls.node_type))
            cls.category = 'Material'

        elif node_type == 'texture':
            self.texture_nodes.append((cls.class_type, cls.node_type))
            cls.category = 'Texture'

        else:
            cls.category = 'Default'


class PropertyGroupRegistry(Registry):
    def __init__(self):
        super(PropertyGroupRegistry, self).__init__()
        self.property_groups = {}

    def add_new_property_class(self, cls, prop_name):
        self.add_new_class(cls)
        self.property_groups[prop_name] = cls


regular_registry = Registry()
shading_node_registry = ShadingNodeRegistry()
property_group_registry = PropertyGroupRegistry()


class Material(object):
    def __init__(self):
        self.node_type = 'material'

    def __call__(self, cls):
        shading_node_registry.add_new_shading_class(cls, self.node_type)
        return cls


class Texture(object):
    def __init__(self):
        self.node_type = 'texture'

    def __call__(self, cls):
        shading_node_registry.add_new_shading_class(cls, self.node_type)
        return cls
