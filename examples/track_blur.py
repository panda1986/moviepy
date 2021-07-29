import pickle

from moviepy.editor import *
from moviepy.video.tools.tracking import manual_tracking
from moviepy.video.tools.tracking import Trajectory

# LOAD THE CLIP (subclip 6'51 - 7'01 of a chaplin movie)
clip = VideoFileClip("./sources/chaplin.mp4")

# MANUAL TRACKING OF THE HEAD

#trajectories = manual_tracking(clip, t1=4, t2=7, fps=6, nobjects=1, savefile="track.txt")
traj = Trajectory.load_list('track.txt')
print (traj[0].tt, traj[0].xx, traj[0].yy)
trackingInf = list(zip(traj[0].tt, traj[0].xx, traj[0].yy))
print (trackingInf)

#定义fx和fy函数：
def fx(t):
    t1 = t2 = None
    for tc in trackingInf:
        if t == tc[0]: #t即为跟踪的帧
            return tc[1]
        elif t > tc[0]: #记录t前面最近的跟踪帧
            t1 = tc
        else:#找到t之后最近的跟踪帧
            if t1: #前面有跟踪帧
                d1 = t - t1[0]
                d2 = tc[0] - t
                d = min(d1, d2)
                return t1[1] if d == d1 else tc[1]
            else: #t应该至少前面有个跟踪帧、后面也有个跟踪帧，否则为异常数据
                return 0

    return tc[1]  #返回x坐标

def fy(t):
    t1 = t2 = None
    for tc in trackingInf:
        if t == tc[0]:
            return tc[2]
        elif t > tc[0]:
            t1 = tc
        else:
            if t1:
                d1 = t - t1[0]
                d2 = tc[0] - t
                d = min(d1, d2)
                if d > 0.5: return 0
                return t1[2] if d == d1 else tc[2]
            else:
                return 0

    return tc[2]#返回y坐标

clip_blurred = clip.fx( vfx.headblur, fx, fy, 30, r_blur=20)
clip_blurred.write_videofile('./blurredChaplin.avi', bitrate="3000k", codec='mpeg4', audio=False)
# IF THE MANUAL TRACKING HAS BEEN PREVIOUSLY DONE,
# LOAD THE TRACKING DATA AND CONVERT IT TO FUNCTIONS x(t),fy(t)

#with open("../../chaplin_txy.dat",'r') as f:
#    fx,fy = to_fxfy( pickle.load(f) )


# BLUR CHAPLIN'S HEAD IN THE CLIP

#clip_blurred = clip.fx( vfx.headblur, fx, fy, 25)


# Generate the text, put in on a grey background

#txt = TextClip("Hey you ! \n You're blurry!", color='grey70',
#               size = clip.size, bg_color='grey20',
#               font = "Century-Schoolbook-Italic", fontsize=40)
               
               
# Concatenate the Chaplin clip with the text clip, add audio

#final = concatenate_videoclips([clip_blurred,txt.set_duration(3)]).\
#          set_audio(clip.audio)

# We write the result to a file. Here we raise the bitrate so that
# the final video is not too ugly.

#final.write_videofile('../../blurredChaplin.avi', bitrate="3000k")
