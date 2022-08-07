import bpy


bprop_map = {
    'float' : bpy.props.FloatProperty,
    'int' : bpy.props.IntProperty,
    'bool' : bpy.props.BoolProperty,
    'string' : bpy.props.StringProperty,
    'fvec' : bpy.props.FloatVectorProperty,
}