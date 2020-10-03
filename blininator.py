print("Welcome to the Blininator 2020")
eggsMin = 1
milkMin = 200
flourMin = 100

eggsAmount = int(input("How many eggs do you have?\n"))
milkAmount = int(input("How much milk do you have, in mililitres?\n"))
flourAmount = int(input("How much flour do you have, in grams?\n"))

if eggsAmount < eggsMin or milkAmount < milkMin or eggsAmount < eggsMin:
    print("No blins for you")
else:
    flourPortion = flourAmount // flourMin
    print("You have " + str(flourPortion) +
    " portions of flour.")
    
    milkPortion = milkAmount // milkMin
    print("You have " + str(milkPortion) + 
    " portions of milk.")
    
    eggsPortion = eggsAmount // eggsMin
    print("You have " + str(eggsPortion) + 
    " portions of eggs.")

if eggsPortion > milkPortion:
    if milkPortion > flourPortion:
        print("The smallest number of blins possible is " + str(flourPortion))
        MinBlin = flourPortion
    else:
        print("The smallest number of blins possible is " + str(milkPortion))
        MinBlin = milkPortion
elif milkPortion > eggsPortion:
    if eggsPortion > flourPortion:
        print("The smallest number of blins possible is " + str(flourPortion))
        MinBlin = flourPortion
    else:
        print("The smallest number of blins possible is " + str(eggsPortion))
        MinBlin = eggsPortion

print("You can make " + str(MinBlin*4) + " blins with your amount of ingredients.")
print("To do this, you will only need " + str(MinBlin * eggsMin) +
" eggs," + str(MinBlin * flourMin) + "g of flour, and " +
 str(MinBlin * milkMin) + "ml of milk.")

print("Goodbye")
