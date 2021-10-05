# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:12:48 2021

@author: Adrián
"""

import speech_recognition as sr
import moviepy.editor as mp
import numpy as np
import os
from pydub import AudioSegment 
# SETUP 

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
        # split_audio = self.audio[t1:t2]
        # split_audio.export(self.folder +'\\Split2' + '\\' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in np.arange(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            # print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')

folder = 'C:\Work\Integra\Video to text'
file = 'mananera2.wav'
split_wav = SplitWavAudioMubin(folder, file)
X = split_wav.multiple_split(min_per_split = .5)
# split_wav.multiple_split(min_per_split = .5)

# SPEECH RECOGNITION

r = sr.Recognizer()

# Many files
directory = 'C:\Work\Integra\Video to text\Split2'

# Exported Splits
# r = sr.Recognizer()
# for filename in os.listdir(directory):
#     if filename.endswith(".wav"): 
#         audio =  sr.AudioFile(directory + '\\' + filename)
#         with audio as source:
#             audio_file = r.record(source)
#         try:
#             result = r.recognize_google(audio_file, language="es-ES")
#         except:
#             result = 'ininteligible'
            
#         s = filename.split('_')[0]
#         with open(directory + '\\' + 'recognized_2.txt', mode = 'a') as file:
#             file.write('\n')
#             file.write(result)        
#         continue
#     else:
#         continue

# Withour writting the splits
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