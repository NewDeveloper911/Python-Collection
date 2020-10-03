fly = input("Can you fly?")
stronk = input("Are you very stong?")
gender = input("What is your gender?")
if fly == "yes":    
    if stronk == "yes":        
        if gender == "male":
            print("You are Superman.")
        else:
            print("You are Wonder Woman.")
    else:
        print("You are Falcon.")

elif fly == "no":    
    if stronk == "yes": 
        if gender == "male":
            print("You are Spider-Man.")
        else:
            print("You are She-Hulk.")
    else:
        print("You aren't a superhero apparently.")    
else:
    print("You need an actual answer: no / yes")
