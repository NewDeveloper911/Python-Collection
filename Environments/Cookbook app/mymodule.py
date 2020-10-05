def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "Nana",
  "age": 15,
  "country": "Ghana"
}

def omin(om):
  om = 2
  print("Minimum onions are " + str(om))
  


def tmin(tm):
  tm = 4
  print("Minimum tomatoes are " + str(tm))



def cmin(cm):
  cm = 10
  print("Minimum peppers are " + str(cm))


def smallest(thesmallest, om, tm, cm):
  onionAmount = int(input("How many onions do you have?\n"))
  onionAmount = onionAmount // om
  tomAmount = int(input("How many tomatoes do you have?\n"))
  tomAmount = tomAmount // tm
  chiliAmount = int(input("How many chillies do you have?\n"))
  chiliAmount = chiliAmount //cm

  if onionAmount == 0 or tomAmount == 0 or chiliAmount == 0:
    print("Forget it. You don't enough ingredients to make a pot of stew")
    quit
    
  if onionAmount < tomAmount and onionAmount < chiliAmount:
    thesmallest = onionAmount
  elif tomAmount < onionAmount and tomAmount < chiliAmount:
    thesmallest = tomAmount
  else:
    thesmallest = chiliAmount

  print("You can make " + str(thesmallest) + " batches of chili, each with a squeeze of lemon and a pinch of salt")
  print("For each batch, you need to blend " + str(thesmallest) + " times, each for about 2 mins")
  print("To do so, you will need " + str(thesmallest * om) + " onions, " + str(thesmallest * tm) + " tomatoes and "  + str(thesmallest * cm) + " peppers.")

