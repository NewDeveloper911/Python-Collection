import time

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "Nana Yaw Brobbey Amfo-Brobbey",
  "age": 15,
  "country": "Ghana"
}

def minimum(fmin, smin, bpmin, strmin, milkmin,omin, vmin):
    print("The minimum amount of flour is: " + str(fmin) + "g.")
    print("The minimum amount of sugar is: " + str(smin) + "g.")
    print("The minimum amount of baking powder is: " + str(bpmin) + "g.")
    print("The minimum amount of diced strawberries is: " + str(strmin) + ".")
    print("The minimum amount of milk is: " + str(milkmin) + "ml.")
    print("The minimum amount of oil is: " + str(omin) + "ml.")
    print("The minimum amount of vanilla extract is: " + str(vmin) + "ml.")
    return fmin, smin, bpmin, strmin, milkmin,omin, vmin

def smallest(thesmallest, fmin, smin, bpmin, strmin, milkmin,omin, vmin):
  flourAmount = int(input("How much flour do you have, in grams?\n"))
  flourAmount = flourAmount // fmin
  
  sugarAmount = int(input("How much sugar do you have, in grams?\n"))
  sugarAmount = sugarAmount // smin
  
  bakingAmount = int(input("How much baking powder do you have, in grams?\n"))
  bakingAmount = bakingAmount // bpmin
  
  strawAmount = int(input("How many strawberries do you have?\n"))
  strawAmount = strawAmount // strmin
  
  milkAmount = int(input("How much milk do you have, in mililitres?\n"))
  milkAmount = milkAmount //milkmin

  oilAmount = int(input("How much oil do you have, in mililitres?\n"))
  oilAmount = oilAmount //omin

  vanillaAmount = int(input("How much vanilla extract do you have, in mililitres?\n"))
  vanillaAmount = vanillaAmount //vmin

  thesmallest = min(fmin, smin, bpmin, strmin, milkmin,omin, vmin)

  if thesmallest == 0:
    print("Forget it. You don't enough ingredients to make any strawberries and cream mug cakes")
    quit
 

  print("You can make " + str(thesmallest) + " batches of strawberries and cream mug cakes, each with an optional topping of whipped cream and an extra strawberry")
  print("For each batch, you need to blend " + str(thesmallest) + " times in a 375ml or larger mug until just combined.\n I'll be back in fifteen seconds")
  time.sleep(15)
  print("To do so, you will need " + str(thesmallest * fmin) + " g of flour, " + str(thesmallest * smin) + " g of sugar, "  + str(thesmallest * bpmin) + " g of baking powder")
  print("You will also need " + str(thesmallest * strmin) + " strawberries, " + str(thesmallest * milkmin) + "ml of milk, " + str(thesmallest * omin) + "ml of oil")
  print("Don't forget to also get " + str(thesmallest * vmin) + "ml of vanilla extract.")
  print("Microwave the mug on high for about 90 seconds(or less, depending on the size of your mug)")
  time.sleep(95)
  print("Wait there a minute. Let the mug cool down for a minute first. When I come back, then you can eat. Please wait a minute for me!")
  time.sleep(55)
  print("Alright, I'm back. Save some for me. Haha, just kidding, I can't eat. However, please enjoy. See you later")

