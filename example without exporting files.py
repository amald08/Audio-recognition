# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:05:46 2021

@author: Adrián
"""

import speech_recognition as sr
import moviepy.editor as mp
import numpy as np
import os
from pydub import AudioSegment 
import io
# SETUP
 

clip = mp.VideoFileClip(r'C:\Work\Integra\Video to text\Harina.mp4')
clip.audio.write_audiofile(r'C:\Work\Integra\Video to text\converted.wav')

# src = r'C:\Work\Integra\Video to text\Mananera_5_julio.mp3'
# dst = r'C:\Work\Integra\Video to text\converted.wav'

# convert wav to mp3                                                            
# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")

# CUT AUDIO
import math

class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        
        self.audio = AudioSegment.from_wav(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        return(split_audio)
        # buf = io.BytesIO()
        # split_audio.export(buf, format="wav")
        # return(buf.getvalue())
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        a =[]
        for i in np.arange(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            a.append(self.single_split(i, i+min_per_split, split_fn))
            # print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')
        return(a)        
        
                
                

folder = 'C:\Work\Integra\Video to text'
file = 'converted.wav'
split_wav = SplitWavAudioMubin(folder, file)
X = split_wav.multiple_split(min_per_split = .5)

# SPEECH RECOGNITION

# audio = sr.AudioFile(r'C:\Work\Integra\Video to text\Split\0.5_converted.wav')


# with audio as source:
#   audio_file = r.record(source)
# result = r.recognize_google(audio_file, language="es-ES")

# # EXPORTING THE RESULT

# # exporting the result 
# with open(r'C:\Work\Integra\Video to text\recognized.txt', mode ='w') as file: 
#    file.write("Recognized Speech:") 
#    file.write("\n") 
#    file.write(result) 
#    print("ready!")

# Many files
directory = 'C:\Work\Integra\Video to text\Split'
r = sr.Recognizer()
for x in X:
    b = io.BytesIO()
    x.export(b, 'wav')
    b.seek(0)
    audio = sr.AudioFile(b)
    with audio as source:
        audio_file = r.record(source)
    try:
        result = r.recognize_google(audio_file, language="es-ES")
    except:
        result = 'No se entiend'
    # result = r.recognize_google(audio_file, language = 'es-Es')
    # s = filename.split('_')[0]
    with open(directory + '\\' + 'harina.txt', mode = 'a') as file:
        file.write('\n')
        file.write(result)        


