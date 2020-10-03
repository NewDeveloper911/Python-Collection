import turtle

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")

side=400
myPen.penup()
myPen.goto(-200,-200) #position cursor at the bootom right of the screen
myPen.pendown()

#Start Spiral
for i in range (1,100):
   myPen.forward(side)
   myPen.left(90)
   side=side-4
