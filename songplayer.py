
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
    for root, dirs, files in os.walk(r'/Users/mac'):
        for name in files:
            if name == songfile:
                print("Now playing - " + songfile)
                play.playsound(os.path.abspath(os.path.join(root, name)))

song = input("Would you like to play a song? If so, which song would you like to play?\n Don't forget to state the directory, if possible\n")
try:
	funkymusic(song)
except:
	print("Unfortunately, we couldn't find and play this song for you")
print("Thanks for utilising this python script")
