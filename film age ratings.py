age = int(input("What is your age?"))
if age >= 18:
    print("You can watch any kind of film. Enjoy!")
elif age >= 15 and age < 18:
    print("You can watch U, PG ,12 ,12A, and 15 rated films.")
elif age >= 12 and age < 15:
    print("You can watch U, PG ,12 and 12A rated films.")
elif age >= 5 and age < 12:
     print("You can watch U and PG  rated films.")
elif age >= 5 and age < 10:
    print("You can only watch U rated films.")
else:
    print("You are too young to watch any kind of film.")
    
