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


