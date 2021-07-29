import os
from moviepy.editor import *
clip = (VideoFileClip("./sources/xafanda_timestamp.flv", audio=False)
        .subclip(10,20))
#clip1 = vfx.blackwhite(clip)
#clip1 = vfx.colorx(clip, 2)
#clip1 = vfx.invert_colors(clip)
#clip1 = vfx.margin(clip, mar=100, color=(255, 0, 0))
#clip1 = vfx.mirror_x(clip)
#clip1 = vfx.resize(clip, (240,320))
#clip1 = vfx.rotate(clip, 90)
#clip1 = vfx.speedx(clip, factor=0.5)  # 1/2 speed
#clip1 = vfx.speedx(clip, factor=2)  # 2 speed
clip1 = vfx.time_symmetrize(clip)
clip1.write_videofile("panda_test_fx.mp4")      