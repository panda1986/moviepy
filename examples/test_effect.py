from moviepy.editor import *

clip = VideoFileClip("./sources/audrey.mp4")
clip.save_frame("./sources/audrey2.png", t=0.20)