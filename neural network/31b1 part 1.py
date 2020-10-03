def problem(x):
    x = 1+(1.0 /  x)
    print(x)

endit = True
number = float(input("Enter  number:"))
problem(number)
endcode = input("Do you want to continue\n enter yes to continue")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
if(endcode.upper() == "YES"):
    endit = False
else:
    endit = True

while(endit == False):
    number = float(input("Enter  number:"))
    problem(number)
    endcode = input("Do you want to continue?\n press enter to continue\n")
    if(endcode.upper() == "YES"):
        endit = False
    else:
        endit = True
    
