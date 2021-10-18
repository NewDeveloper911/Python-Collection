import pdb

pdb.set_trace()

year = int(input("Which year were you born in?"))
age = ( 2021 - year )
if age >= 16 and age <= 32:
    print("You can join the army.")
else:
    print("You can't join the army.")
