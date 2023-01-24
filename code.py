from moviepy.editor import *
import random2

background = ['1', '2', '3', '4', '5', '6', '9']

#audioclip = AudioFileClip("background_music.mp3")
sound = AudioFileClip("open.mp3")
#clip = VideoFileClip('C:\\Users\\Dell\\Desktop\\content\\backgrounds\\' + random2.choice(background) + '.mp4')
clip = VideoFileClip('C:\\Users\\Dell\\Desktop\\content\\backgrounds\\green.mp4')
#logo = ImageClip("logo.png").set_duration(25)
#logo.margin(top=20, left=20, opacity=0)
#logo.set_pos('left','top')

txt_clip = TextClip("Test #1", fontsize = 120, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color="black").set_duration(2.2)
txt_clip = txt_clip.set_pos('center')
txt_clip.set_start(0)