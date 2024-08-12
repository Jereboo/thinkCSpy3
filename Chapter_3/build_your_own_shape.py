#A program that allows the user to input the number of sides, length, color, and background of a shape
import turtle
import random

print("Let's build our own custom shape!")

sides = int(input("How many sides do you want your shape to have? "))
length = int(input("How long do you want the sides to be? (Pick any number between 20-75) "))
color = str(input("What color do you want the border to be? "))
fill_color = str(input("What color do you want the inside of the shape to be? "))

wn = turtle.Screen()
shape = turtle.Turtle()

shape.color(color)
shape.fillcolor(fill_color)

shape.begin_fill()
for i in range(sides):
    shape.forward(length)
    shape.right(random.randrange(0, 361))
shape.end_fill()

turtle.exitonclick()
