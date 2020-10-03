subject = input("Which subject would you like to test yourself on today?\n")
if subject.upper() == "BIOLOGY":
    import biologyquiz
elif subject.upper() == "CHEMISTRY":
    import chemistryquiz
elif subject.upper() == "PHYSICS":
    import physicsquiz
elif subject.upper() == "BUSINESS":
    import businessquiz
else:
   quit()

    
    
