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
sent = 'When you click . You can open new "virtual" desktop.'
words = sent.split()
word = words[0]
t1 = TextClip(word, fontsize = 150, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color='black').set_start(2.5)
t1 = t1.set_pos('center')
t1 = t1.set_end(2.8)
t1.set_duration(0.2)

word = words[1]
t11 = TextClip(word, fontsize = 150, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color='black').set_start(2.8)
t11 = t11.set_pos('center')
t11 = t11.set_end(3.0999999999999996)
t11.set_duration(0.2)

word = words[2]
t111 = TextClip(word, fontsize = 150, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color='black').set_start(3.1)
t111 = t111.set_pos('center')
t111 = t111.set_end(3.4)
t111.set_duration(0.2)

word = words[3]
t1111 = TextClip(word, fontsize = 150, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color='black').set_start(3.4)
t1111 = t1111.set_pos('center')
t1111 = t1111.set_end(4.3999999999999995)
t1111.set_duration(0.2)

word = words[4]
t11111 = TextClip(word, fontsize = 150, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color='black').set_start(4.4)
t11111 = t11111.set_pos('center')
t11111 = t11111.set_end(4.7)
t11111.set_duration(0.2)

word = words[5]
t111111 = TextClip(word, fontsize = 150, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color='black').set_start(4.7)
t111111 = t111111.set_pos('center')
t111111 = t111111.set_end(5.0)
t111111.set_duration(0.2)

word = words[6]
t1111111 = TextClip(word, fontsize = 150, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color='black').set_start(5.0)
t1111111 = t1111111.set_pos('center')
t1111111 = t1111111.set_end(5.3)
t1111111.set_duration(0.2)

word = words[7]
t11111111 = TextClip(word, fontsize = 150, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color='black').set_start(5.3)
t11111111 = t11111111.set_pos('center')
t11111111 = t11111111.set_end(5.6)
t11111111.set_duration(0.2)

word = words[8]
t111111111 = TextClip(word, fontsize = 150, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color='black').set_start(5.6)
t111111111 = t111111111.set_pos('center')
t111111111 = t111111111.set_end(5.8999999999999995)
t111111111.set_duration(0.2)

word = words[9]
t1111111111 = TextClip(word, fontsize = 150, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color='black').set_start(5.9)
t1111111111 = t1111111111.set_pos('center')
t1111111111 = t1111111111.set_end(6.8999999999999995)
t1111111111.set_duration(0.2)

video = CompositeVideoClip([clip, txt_clip, t1, t11, t111, t1111, t11111, t111111, t1111111, t11111111, t111111111, t1111111111]).set_duration(6.8999999999999995)
video = vfx.fadeout(video, duration=0.6, final_color=[0,0,0])

video.write_videofile("test.mp4")