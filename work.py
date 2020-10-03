english = ['a', 'b' ,'c', 'd', 'e' ,'f', 'g', 'h']
countries = ["Ghana", "Guyana" ,"Egypt" ,"Algeria", "South Africa", "India", "Pakistan"]
colour = ['blue', 'orange' ,'red', 'green', 'purple', 'yellow', 'indigo']
fav_subjects = ['PE', 'Computer Science']

print(countries[2])
print(english[6])
print(colour[1])
print(fav_subjects[0])

english.remove('a')
english.remove('b')
english.remove('c')
english.remove('d')
english.remove('e')

english.append('h')
english.append('i')
english.append('j')
english.append('k')
english.append('l')


fav_subjects.append('Maths')
fav_subjects.append('Business')
fav_subjects.append('D&T')

countries.remove("Ghana")
countries.remove("Guyana")
countries.remove("Egypt")

countries.append('Accra')
countries.append('Paris')
countries.append('Dubai')

if "purple" in colour:
    print(colour)
else:
    print("Purple isn’t in the list...")

if "red" in colour:
    print("Red is in my list")
else:
    mylist.append("red")
print("Red has been added to the list")

