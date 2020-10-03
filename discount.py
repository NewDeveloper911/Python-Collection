print("It's discount day!")
price = float(input("What is the price of the product?\n"))
if price <= 10:
    print("The final price is " , price , ".")
elif price >= 11 and price <= 50:
    print("The final price is " ,(price - (price / 10)) , ".")
elif price >= 51 and price <=100:
    print("The final price is ", (price - (price / 5)) , ".")
else:
    print("The final price is ", (price - (price / 2)) , ".")


'''
shopping = input("Do you still want to shop?\n")
if shopping.upper() == "YES":
    still = True
    while still == True:
        nextprice = float(input("What is the price of the next product that you want to buy?\n"))
        if price <= 10:
            print("The final price is " , nextprice , ".")
            finalprice = nextprice
        elif nextprice >= 11 and nextprice <= 50:
            print("The final price is " ,(nextprice - (nextprice / 10)) , ".")
            finalprice = nextprice
        elif nextprice >= 51 and nextprice <=100:
            print("The final price is ", (nextprice - (nextprice / 5)) , ".")
            finalprice = nextprice
        else:
            print("The final price is ", (nextprice - (nextprice / 2)) , ".")
            finalprice = nextprice

        cunt = input("Do you still want to shop?\n")
        if cunt.upper() == "NO":
            print("You are expected to pay " + str(price + finalprice) + "." )
            still = False
            
'''
