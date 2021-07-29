# https://github.com/jlindo33/moviepy/blob/master/examples/headblur.py
from moviepy.editor import *
from moviepy.video.tools.interpolators import Trajectory
from moviepy.video.tools.tracking import manual_tracking

# LOAD THE CLIP (subclip 6'51 - 7'01 of a chaplin movie)
clip = VideoFileClip("./sources/chaplin.mp4")

# MANUAL TRACKING OF THE HEAD

# the next line is for the manual tracking and its saving
# to a file, it must be commented once the tracking has been done
# (after the first run of the script for instance).
# Note that we save the list (ti, xi, yi), not the functions fx and fy

#manual_tracking(clip, t1=4, t2=7, fps=6, savefile="blurred_trajectory.txt")

# IF THE MANUAL TRACKING HAS BEEN PREVIOUSLY DONE,
# LOAD THE TRACKING DATA AND CONVERT IT TO TRAJECTORY INTERPOLATORS fx(t), fy(t)

traj = Trajectory.from_file("blurred_trajectory.txt")
# BLUR CHAPLIN'S HEAD IN THE CLIP PASSING xi(t) and yi(t) FUNCTIONS

clip_blurred = clip.fx(vfx.headblur, traj.xi, traj.yi, 25, r_blur=20)
clip_blurred.write_videofile("blurredChaplin.mp4", audio=False)