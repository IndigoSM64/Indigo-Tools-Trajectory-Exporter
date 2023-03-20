


bl_info = {
    "name": "Indigo Tools",
    "author": "Indigo",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "View3D > UI > Indigo Tools",
    "description": "tools for hackers SM64",
    "warning": "",
    "doc_url": "",
    "category": "SM64 Tools"
}

from .Trajectory_Exporter import *
from .Trajectory_Exporter_Cutscene import *
import bpy
from bpy.utils import register_class, unregister_class


def register():
    trajectory_register()
    cutscene_trajectory_register()
    
def unregister():
    trajectory_unregister()
    cutscene_trajectory_unregister()
