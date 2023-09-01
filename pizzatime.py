orderId = 0
confirm = ""
while confirm.upper() != "Y":
    size = ""
    base = ""
    confirm = ""
 
    toppings = []
    size = input("Please input a size: small, medium or large\n")
    while size.upper() != "SMALL" and size.upper() != "MEDIUM" and size.upper() != "LARGE":
        rsize = input("Error: please enter a correct size: small, medium or large\n")
        if rsize.upper() == "SMALL" or rsize.upper() == "MEDIUM" or rsize.upper() == "LARGE":
            break
        
    base = input("Please input a base: thick or thin\n")
    while base.upper() != "THICK" and base.upper() != "THIN":
        rbase = input("Error: please enter a correct base: thick or thin\n")
        if rbase.upper() == "THICK" or rbase.upper() == "THIN":
            break
            
 
    toppingNum = int(input("How many toppings would you like? Maximum is 3\n"))
    if toppingNum > 0 and toppingNum <= 3:
        for i in range(toppingNum):
            toppingchoice =  input("Please input a topping:\n")
            while toppingchoice.upper() not in ["PEPPERONI","CHICKEN","EXTRA CHEESE","MUSHROOMS","SPINACH","OLIVES"]:
                rtoppingchoice = input("ERROR: Please enter a valid choice\n")
                if rtoppingchoice.upper() in ["PEPPERONI","CHICKEN","EXTRA CHEESE","MUSHROOMS","SPINACH","OLIVES"]:
                    break
                    
            if toppingchoice.upper() not in ["PEPPERONI","CHICKEN","EXTRA CHEESE","MUSHROOMS","SPINACH","OLIVES"]:
                toppings.append(toppingchoice)
            else:
                toppings.append(rtoppingchoice)
                
    elif toppingNum < 0 or toppingNum > 3:
        rtoppingNum = int(input("2) How many toppings would you like? Maximum is 3\n"))
        while rtoppingNum < 0 or rtoppingNum > 3:
            srtopNum = int(input("3) How many toppings would you like? Maximum is 3\n"))
            if srtopNum > 0 and srtopNum <= 3:
                toppingNum = srtopNum
                for i in range(toppingNum):
                    toppingchoice =  input("Please input a topping:\n")
                    while toppingchoice.upper() not in ["PEPPERONI","CHICKEN","EXTRA CHEESE","MUSHROOMS","SPINACH","OLIVES"]:
                        rtoppingchoice = input("ERROR: Please enter a valid choice\n")
                        if rtoppingchoice.upper() not in ["PEPPERONI","CHICKEN","EXTRA CHEESE","MUSHROOMS","SPINACH","OLIVES"]:
                            toppingNum = srtopNum
                            break
                    if toppingchoice.upper() not in ["PEPPERONI","CHICKEN","EXTRA CHEESE","MUSHROOMS","SPINACH","OLIVES"]:
                        toppings.append(toppingchoice)
                    else:
                        toppings.append(rtoppingchoice)
        
    else:
        print("Do not press enter without inputting a number for the amount of toppings")
        quit()
     
    if toppingNum == 1:
        print("Your order is a pizza of size " + size + ", with a base of " + base + " and your toppings are " + toppings[0] + ".")
    elif toppingNum == 2:
        print("Your order is a pizza of size " + size + ", with a base of " + base + " and your toppings are " + toppings[0] + " and " + toppings[1] + ".")
    else:
        print("Your order is a pizza of size " + size + ", with a base of " + base  + " and your toppings are " + toppings[0] + "," + toppings[1] + " & " + toppings[2] + ".")

 
    confirm = input("Is this your desired pizza? Press 'y' for yes and 'n' for no")
 
orderId += 1
print("Your order ID is " + str(orderId))
