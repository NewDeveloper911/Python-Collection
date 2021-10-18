import speech_recognition as sr
#from gtts import gTTS
import pyttsx3
import os
import time
import playsound as play

stored_songs = []
saved_songs = []

def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+50)
    engine.say(text)
    engine.runAndWait()

def funkymusic(songfile):
    #The following line checks for all song file locations on Mac
    #The line below will show to code for Windows users
    #for root, dirs, files in os.walk(r'/C:'):
    for root, dirs, files in os.walk(r'/Users/mac'):
        for name in files:
            if name not in stored_songs and name[-4:] == ".mp3" or name[-4:] == ".wav":
                stored_songs.append(name)
            if songfile.upper() in name.upper() and name[-4:] == ".mp3" or name[-4:] == ".wav":
                try:
                    print("Now playing - " + name)
                    speak("Now playing - " + name)
                except:
                    print("Now playing - " + name)
                play.playsound(os.path.abspath(os.path.join(root, name)))

def save_songs():
    #The following line checks for all song file locations on Mac and saves it to an array
    #The line below will show to code for Windows users
    #for root, dirs, files in os.walk(r'/C:'):
    for root, dirs, files in os.walk(r'/Users/mac'):
        for name in files:
            if name not in stored_songs and name[-4:] == ".mp3" or name[-4:] == ".wav":
                stored_songs.append(name)
                saved_songs.append(name)

def play_all_songs():
    #The following line checks for all song file locations on Mac and saves it to an array
    #The line below will show to code for Windows users
    #for root, dirs, files in os.walk(r'/C:'):
    for root, dirs, files in os.walk(r'/Users/mac'):
        for name in files:
            if name[-4:] == ".mp3" or name[-4:] == ".wav":
                play.playsound(os.path.abspath(os.path.join(root, name)))
