import time

def greeting(name):
    print("Oh well hello " + name + "! Nice to see you.")
    
def cabmin(cabm):
  cabm = 0.6666
  print("Minimum cabbage are " + str(cabm))
  


def carmin(carm):
  carm = 2
  print("Minimum carrots are " + str(carm))



def cookmin(com):
  com = 200
  print("Minimum amount of cooking cream is " + str(com) + 'ml')


              
def smallest(thesmallest):
  cabAmount = float(input("How much cabbage do you have?\n"))
  cabm = 0.6666
  cabAmount = cabAmount // cabm
  carAmount = float(input("How many carrots do you have?\n"))
  carm = 2
  carAmount = carAmount // carm
  cookAmount = float(input("How much cooking cream or coconut milk do you have?\n"))
  com = 500
  cookAmount = cookAmount //com

  if cabAmount < carAmount and cabAmount < cookAmount:
    thesmallest = cabAmount
  elif carAmount < cabAmount and carAmount < cookAmount:
    thesmallest = carAmount
  else:
    thesmallest = cookAmount

  print("You can make " + str(thesmallest) + " pots of stew or sauce, each with a squeeze of lemon and a pinch of salt")
  print("First shred " + str(thesmallest * cabm) + " of the cabbage approximately")
  print("Then, dice "+ str( carm  ) + " carrots approximately")
  print("If you happen to have any fish, add about " + str(400 * thesmallest) + "g worth of fish to a pan.")
  print("Leftover stews can also help but always sniff to check if it is still good")

  print("Now add the carrots and stir for about " + str( 4 )  + "mins or until soft")
  time.sleep(10)
  print("Now add the cabbage and stir for about " + str( 4) + " mins or until beginning to golden. ")
  time.sleep(5)
  print("Finally, douse it all in " + str(com) + "mls of cooking cream or coconut milk, add some pepper and save the rest")
  time.sleep(1)
  print("Remember to use a dash of nutmeg, rosemary, cloves, cayenne peppers and pepper corns to add as I quote from Lazarbeam,'that little bit of flavour")
  time.sleep(30)
def confidence(confid):
    confid = input("How are you feeling about this stew? Enter 'ok' or 'good' if you are feeling confident")
    if confid.upper() == "OK" or confid.upper() == "GOOD":
        print("Good job. Just imagine how good this stew is going to be. I'll be back when you're done")
    else:
        print("Don't worry. You'll get the hang of it at some point. I'll be back soon, don't worry. Edit the cookbook code when you are more confident")
    time.sleep(300)
    
def final(sauce):
    
    print("Now, that smells delicious. I wish that I could have some of that but I have no soul. Bummer. Don't worry about me and just enjoy your meal")
    print("Re-run this program until you have made enough batches to satisfy yourself and now, I shall bid you goodbye and wish you well. Goodbye!")
    
