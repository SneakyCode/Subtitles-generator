import shutil

deploy = 'video = CompositeVideoClip([clip, txt_clip'
#audio = 'audioclip = CompositeAudioClip([sound, audioclip]).set_duration('
encode = '\nvideo.write_videofile("test.mp4")'
sent = 'When you click . You can open new "virtual" desktop.'

x = 0
name = 't'
words = sent.split(' ')
word = words[0]
duration = 2.2

res = sent.count(' ')+1

shutil.copyfile('code.py','content.py')
f = open('content.py', 'a')
f.write('\nsent = ' + "'" + sent + "'")
f.write('\nwords = sent.split(' ')')

while not x == res:
	name = name + str(1)
	duration = duration + 0.3
	f.write('\nword = words[' + str(x) + ']')
	script1 = '\n' + name + ' = ' + "TextClip(word, fontsize = 150, font = 'Franklin-Gothic-Medium', color='white', stroke_width = 5, stroke_color='black').set_start(" + str(round(duration, 1)) + ")" + "\n"
	script2 = script1 + name + " = " + name + ".set_pos('center')\n"
	script = script2 + name + " = " + name + ".set_end(" + str(round(duration, 1) + 0.3) + ")\n"
	if '#' in words[x] or '.' in words[x] or '!' in words[x] or ':' in words[x] or '?' in words[x] or ',' in words[x] or '-' in words[x]:
		duration = duration + 0.7
		script = script2 + name + " = " + name + ".set_end(" + str(round(duration, 1) + 0.3) + ")\n"
	script = script + name + ".set_duration(0.2)\n"
	f.write(script)
	deploy = deploy + ', ' + name
	x += 1

deploy = deploy + ']).set_duration(' + str(round(duration, 1) + 0.3) + ')'
#audio = audio + str(round(duration, 1) + 0.3) + ')'
f.write('\n' + deploy + '\n' + 'video = vfx.fadeout(video, duration=0.6, final_color=[0,0,0])' +'\n' + encode)