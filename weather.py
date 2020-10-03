temperature = int(input("What is the temperature now?\n"))
weather = input("What is the weather today?\n")
if temperature >= 21 and temperature < 30:
    print("At least the temperature seems ok.\n")
    outside = input("What are you going to do today outside?\n")
    if outside == "nothing":
        print("That's honestly a shame.\n")
    else:
        activity = input("Well,what are you going to do today?\n")
        print("That seems enjoyable. I wish that I could" + activity + "but I can't as I am only a piece of software within a fixed hardware casing.\n")
elif temperature >= 30 and (weather == "good" or weather == "sunny" or weather == "ok" or weather == "calm"):
    print("It seems like a beautiful day out there. Why aren't you enjoying it?\n")
    reason = input("Why?\n")
    if reason == "cus" or reason == "i said so":
        print("That's a rubbish excuse\n")
    else:
        print("That seems quite well justified.\n")
elif temperature >= 40 and (weather == "hot" or weather == "boiling"):
    print("My goodness, that's boiling\n")
else:
    print("Yeesh, it seems terrible out there.\n")
