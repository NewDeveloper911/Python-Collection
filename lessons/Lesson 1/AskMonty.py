# Ask Monty
# Twinkl - Introduction to Python

import random
question = ""

phrases = [" why now" , " i know right, ")

while question != "stop":
    question = input("Ask Monty a question (or type stop to finish): ")
    if question == "stop":
        print("Goodbye!")
        break
    else:
        print(phrases[random.randrange(1,len(phrases)-1)])
        print("")


input()        
