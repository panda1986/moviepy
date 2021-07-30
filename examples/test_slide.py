from moviepy.editor import *
clip = VideoFileClip("./sources/xafanda_timestamp.flv").subclip(10, 16).fx(vfx.fadein, duration=2)
# clip2 = VideoFileClip("./sources/xafanda_timestamp.flv").subclip(30, 36)
# clips = [clip, clip2]
# slided_clips = [CompositeVideoClip([
#                         clip.fx(transfx.slide_in, duration=2, side='left')])
#                         for clip in clips]
# final_clip = concatenate_videoclips( slided_clips)
clip.write_videofile("1.mp4", audio=False)