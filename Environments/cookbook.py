print("Access names to the recipes is as follows, please copy them below:\n pepper - red chili pepper recipe \n cabsauce - vegetable pot stew")
print(" mugcake - Strawberries and cream mug cakes\n")
recipe = input("What would you like to eat today?\n")
if recipe.upper() == "PEPPER":
    import mymodule as mx
    mx.greeting("Nana")

    mx.omin(2)

    mx.tmin(4)

    mx.cmin(10)

    mx.smallest(0)
elif recipe.upper() == "CABSAUCE":
    import sauce as mx
    mx.greeting("Nana")

    mx.cabmin(0.6666)

    mx.carmin(2)

    mx.cookmin(200)

    mx.smallest(0)

    mx.confidence("OK")

    mx.final("sauce")
elif recipe.upper() == "MUGCAKE":
    import mugcake as mug

    mug.greeting("Yaw Brobbey")
    print("For the amounts below, remember that a teaspoon is 5ml and a tablespoon is 15ml")
    mug.minimum(60, 45, 2.5, 2, 45, 15, 5)
    mug.smallest(0,60, 45, 2.5, 2, 45, 15, 5)
else:
    print("Updates pending")
