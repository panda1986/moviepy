import os
from moviepy.editor import *

clip = (VideoFileClip("./sources/xafanda_timestamp.flv", audio=False)
        .subclip(10,30))
        #.crop(x1=332, x2=910, y2=686))
    
#edited_left = clip.fx(vfx.mirror_x)   
dancing_knights = (clips_array([[clip, clip]])
                   .fadein(3).fadeout(3))

dancing_knights.write_videofile("clips_array.mp4")