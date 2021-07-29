import os
from moviepy.editor import *

charade = VideoFileClip("./sources/xafanda_timestamp.flv")
tfreeze = cvsecs(37)

clip_before = charade.coreader().subclip(tfreeze-3, tfreeze)
clip_after = charade.coreader().subclip(tfreeze, tfreeze+3)

# the frame to freeze
im_freeze = charade.to_ImageClip(tfreeze)
painting = (charade.fx(vfx.painting, saturation = 1.6, black=0.006).to_ImageClip(tfreeze))

txt = TextClip('Audrey', font='Amiri-regular', fontsize=35)
painting_txt = (CompositeVideoClip([painting,txt.set_pos((10,180))])
                   .add_mask()
                   .set_duration(3)
                   .crossfadein( 0.5)
                   .crossfadeout( 0.5))

# FADEIN/FADEOUT EFFECT ON THE PAINTED IMAGE
painting_fading = CompositeVideoClip([im_freeze,painting_txt])

# FINAL CLIP AND RENDERING

final_clip =  concatenate_videoclips([ clip_before,
                            painting_fading.set_duration(3),
                            clip_after])

final_clip.write_videofile('./audrey.avi',fps=charade.fps,
                        codec = "mpeg4", bitrate="800k", audio=False)