import math

"""
There are many advantages in using an object-oriented programming approach, including the following:

 Programs are written as a series of modules based on objects or groups of objects, which makes it easy to modify or
maintain software should a fault develop or a specification change be necessary.
 The modular nature of using OOP techniques is useful in developing a system where programmers can be given tasks
to develop independently.
 New functionality can be added to a program by simply creating a new class or object.
 A class is only concerned with the data defined within it, so it is unlikely to access any other program data
accidentally.
 Data can be hidden within the class that accesses it, providing greater system security.
 Objects can be set up to inherit attributes and methods to create reusable code in the original program they were
developed for as well as in other object-oriented programs.
 OOP code can be used to create code in software libraries for easy reuse.
"""

#Encapsulation in OOP allows data and functions and properties to be capsulated within objects
'''
    Reduces complexity
    Increases reusability - Can have several objects of the same type
'''
#Abstraction removes unnecessary detail

#Inheritance allows several objects to inherit/borrow certain functions and properties from other objects

'''
    Eliminate redundant code
'''

#This section of code outlines the encapsulation of the objects Student and Course
"""
class Student():
    def  __init__(self, name, age, grade):
        #Initialise the properties/attributes of the object being called
        self.name = name
        self.age = age
        self.grade = grade

    #Methods which can interact with the object
    def get_grade(self):
        return self.grade

class Course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, Student):
        if len(self.students) < self.max_students:
            self.students.append(Student)
            return True
        return False

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total/len(self.students)

Nana = Student("Nana", 16, 89)
Abena = Student("Abena", 15, 67)
Memer = Student("Meme", 21, 69)

compSci = Course("Computer Science", 2)
compSci.add_student(Nana)
compSci.add_student(Abena)
print(compSci.students[0].name)
print(compSci.get_average_grade())
"""

#This section will outline more of the abstraction and inheritance involved in OOP
'''
 class Youtuber():
    #This class is an abstraction of generalisation where the below classes are but types of Youtubers
    #This is known as abstraction by generalisation
    def __init__(self, channel_name,name,  subscribers, channel_Age, age, views):
        self.channel_name = channel_name
        self.name = name
        self.subscribers = subscribers
        self.channel_Age = channel_Age
        self.age = age
        self.views = views

    def intro(self):
        print(f"""Hello there. It's me, {self.channel_name}, or rather my real name is {self.name}.
My channel has garnered a whopping {self.subscribers} subscribers and {self.views} views in only {self.channel_Age} years.
        """)

    def content(self):
        print("I just make content for all sorts of people to enjoy, man.\n")
'''
#The classes which inherit from Youtuber
'''
class Prankster(Youtuber):
    def __init__(self, channel_name , name, subscribers, channel_Age, age, views, peoplePranked):
        #No need to redefine attributes defined in the base upper class (known as super)
        super().__init__(channel_name, name, subscribers, channel_Age, age, views)
        self.peoplePranked = peoplePranked

    def prankCount(self):
        print(f"I have pranked {self.peoplePranked} fools while doing my thing on the streets. Get on my level!")

    def content(self):
        print(f"It's just a prank, bro. You just got schooled by {self.channel_name}\n")

class Commentator(Youtuber):
    def content(self):
        print(f"Hey, it's {self.channel_name} here with another hot take on another controversial issue.")

#Each of these are instances of classes - objects
JackSepticEye = Youtuber("Jacksepticeye", "Sean McLaughlin", 16000000,5,32,384971325)
Fousey = Prankster("FouseyTube", "Faisal Ahmed", 18247239, 10, 41, 379180479, 879345)
Fousey.prankCount()
Pyrocynical = Commentator("Pyrocynical", "Niall Walkins", 4790000,8,27,17492739)'''

#This section will go through the process of class attributes

'''
class Person:
    #This variable not near a self is part of the class in general, not just instances
    #Applies to all instances and can be changed by all instances
    #Class attribute
    number_of_people = 0
    inevitability_of_death = True

    def __init__(self, name):
        self.name = name
        Person.add_person()

    #Applies to class(cls) itself
    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Paim")
p2 = Person("Agony")
print(Person.get_number_of_people()) 
'''

#This section will go through static methods
class Maths:
    #These methods can be accessed even without making an instance of Maths
    @staticmethod
    def quadratic(a,b,c):
        if b**2 - 4*a*c > 0:
            print("There are two solutions/roots in this equation")
            return (-b + math.sqrt(b**2 - 4*a*c))/2*a, (-b - math.sqrt(b**2 - 4*a*c))/2*a
        elif b**2 - 4*a*c == 0:
            print("There is a repeated root in this equation, so only one solution")
            return (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        else:
            return "Not possible"

print(Maths.quadratic(7,6,1))