import speech_recognition as sr
#import goslate

from googletrans import Translator
import fleep


translator = Translator()

text=''
info=''
r = sr.Recognizer()
try:
	audio = 'demo.wav'
	# with open('hdhswamishree1.wav', "rb") as file:
 	#info = fleep.get(file.read(128))
except Exception as e1:
	print(e1)
 

fo = open('file1.txt','w+',encoding='utf-8')
# if info.extension==['wav']:
	
with sr.AudioFile(audio) as source:
	print("Please wait......")
	audio = r.record(source)

	print('Please wait......')
	print(audio,source)
try:
	text = r.recognize_google(audio,language='gu-IN')
	# abc = text.decode('utf-8')
	# get = text.read()
	print (text)
	fo.write(text)
	print("Successfully")
	
except Exception as e:
	print(e)
# else:
# print(info.extension)
# print("PLEASE UPLOAD ONLY .WAV FILE")


