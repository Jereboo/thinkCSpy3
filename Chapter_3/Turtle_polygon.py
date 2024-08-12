#A Program to makes a turtle draw an equilateral triangle, square, hexagon, and octagon using for loops
import turtle

wn = turtle.Screen()
triangle = turtle.Turtle()
square = turtle.Turtle()
hexagon = turtle.Turtle()
octagon = turtle.Turtle()

for i in range(3):
    triangle.forward(50)
    triangle.left(120)

for i in range(4):
	square.forward(50)
	square.right(90)

for i in range(6):
    hexagon.backward(50) #or hexagon.forwards(50)
    hexagon.right(60) #or hexagon.right(120)

for i in range(8):
    octagon.backward(50) #or octagon.forwards(50)
    octagon.left(45) #or octagon.left(135)

turtle.exitonclick()