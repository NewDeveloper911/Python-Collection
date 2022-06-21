# Python program to show 
# how to convert text to speech 
import pyttsx3
import PyPDF2
import os
import json

def search(filename):
    for root, dirs, files in os.walk(r'/'):
        for name in files:
            if ".pdf" in name:
                print(name)
            if name == filename:
                print("The file named: " + filename + " has been successfully located")
                return os.path.abspath(os.path.join(root, name))

def listnames(voices):
    for voice in voices:
        print(voice.name + ", " + str(voices.index(voice)))

def searchfor(voicename):
    for i in voices:
        if i.name == voicename:
            print(voicename + " is located at " + str(voices.index(i)))
            converter.setProperty('voice', i.id)
        else:
            continue
        
book = open(search(input("What kind of book do you wish to read?")), 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("This PDF has " + str(pages) + " number of pages.")

# Initialize the converter 
converter = pyttsx3.init() 

# Set properties before adding 
# Things to say 

#searches for all voice types
voices = converter.getProperty('voices')
# Sets speed percent 
# Can be more than 100 
converter.setProperty('rate', 200) 
# Set volume 0-1 
converter.setProperty('volume', 0.3) 
#Sets the voice to sound like whoever I want
converter.setProperty('voice', voices[1].id)

# Queue the entered text 
# There will be a pause between 
# each one like a pause in 
# a sentence

searchfor("Fiona")
listnames(voices)

converter.runAndWait()
pagetoread = pdfReader.getPage(62)
text = pagetoread.extractText()
converter.say(text)
#This can be used to read out an extract from a pdf

# Empties the say() queue 
# Program will not continue 
# until all speech is done talking 
converter.runAndWait() 
