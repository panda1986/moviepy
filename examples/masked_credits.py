from moviepy.editor import *
from moviepy.video.tools.credits import credits1

# Load the mountains clip, cut it, slow it down, make it look darker
clip = (VideoFileClip('./sources/xafanda_timestamp.flv', audio=False)
           .subclip(10,20)
           .speedx(1)
           .fx(vfx.colorx, 0.7))

# Save the first frame to later make a mask with GIMP (only once)
#~ clip.save_frame('../../credits/mountainMask2.png')


# Load the mountain mask made with GIMP
mountainmask = ImageClip('./sources/logo.png',ismask=True)

# Generate the credits from a text file
credits = credits1('./sources/credits.txt',3*clip.w/4)
scrolling_credits = credits.set_position(lambda t:('center',t*12))


# Make the credits scroll. Here, 10 pixels per second
final = CompositeVideoClip([clip,
                            scrolling_credits,
                            clip.set_mask(mountainmask)])
                            
final.subclip(6,10).write_videofile("./credits_mountains.mp4")
