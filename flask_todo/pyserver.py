import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound as play

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    play.playsound(filename)

def funkymusic(songfile):
    for root, dirs, files in os.walk(r'D:\Nanayaw\Demo Songs'): # This directory is just where my songs are. change code to suit your website
        for name in files:
            if name == songfile:
                print("Now playing - " + songfile)
                play.playsound(os.path.abspath(os.path.join(root, name)))



