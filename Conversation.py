import time
time.sleep(3)
mood = input("Nice to meet you. How are you? \n")
if mood == "good" or mood == "ok" or mood == "okay":
    print("You're ", mood ,"? Now, I'm ", mood ," as well.")   
else:
    curious = input("You seem quite moody today. Want to tell me what happened? \n")
    if curious == "yes" or curious == "yeah":
        time.sleep(20)
        print("No need to type. I honestly don't care.")
    else:
        print("Ok then. Keep your secrets.")

