bl_info = {
    "name": "Insert Video File",
    "author": "Aditya Nugroho",
    "version": (1, 0),
    "blender": (2, 7),
    "location": "Video Sequence Editor > Property Panel (N-key)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "https://github.com/AdityaNSukarsono/blenderAddons",
    "category": "Video Sequence Editor"}

import bpy, os

class insert(bpy.types.Operator):
    bl_idname = "scene.invideo"
    bl_label = "Insert Video"

    def execute(self, context):
        episode_path = bpy.path.abspath("C:\\Videos")
        episode_list = os.listdir(episode_path)
        episode_sort = sorted(episode_list)
        first_frame=0
        last_frame=0
        for v in [f for f in episode_sort if f.endswith('.mov')]:
            movs = os.path.join(episode_path,v)
            start_frame = (last_frame)+first_frame
            bpy.ops.sequencer.movie_strip_add(filepath=movs, frame_start=start_frame, channel=1)
            first_frame = bpy.context.scene.sequence_editor.sequences_all[v].frame_start
            last_frame = bpy.context.scene.sequence_editor.sequences_all[v].frame_final_duration
        return{'FINISHED'}

class insertVideo(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "My Tools"
    bl_idname = "my.panel"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Movie File")
        row = layout.row()
        row.operator("scene.invideo", text="Insert Video")

def register():
    bpy.utils.register_class(insertVideo)
    bpy.utils.register_class(insert)


def unregister():
    bpy.utils.unregister_class(insertVideo)
    bpy.utils.unregister_class(insert)


if __name__ == "__main__":
    register()