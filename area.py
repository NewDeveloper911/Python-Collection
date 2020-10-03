shape = input("Which shape do you want to find the area of: square, triangle, circle or rectangle.\n")
measurement = input("What is the measurement that you want to use?\n")
length = float(input("What is the length of the shape?\n"))
height = float(input("What is the height of the shape?\n"))
radius = float(input("If the shape is a circle, what is the radius?\n"))
pi = 3.14159265359
if shape == "square":
    area = ( length * height)
elif shape == "triangle":
    area = (0.5 *(length * height))
elif shape == "circle":
    area = (pi * (radius * radius))
else:
    area = ( length * height )
print(" The area of your " , shape ," is " , area , measurement ,".")

              
