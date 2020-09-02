import os
from pydub import AudioSegment
from playsound import playsound

# files                                                                         
src = "speech.mp4"
dst = "speech.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export("speech1.wav", format="wav")

# playsound('transcript.wav')