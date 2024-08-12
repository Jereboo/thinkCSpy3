#A program to draw a simple 5 pointed star w/ a length of 100 for each side
import turtle

def drawStar(t, sz):
    for i in range(5):
        t.forward(sz)
        t.right(144)
    t.penup()
    t.forward(200)
    t.right(144)
    t.pendown()

def drawMultipleStars(t, sz, st):
    for i in range(int(st)):
        drawStar(t, sz)

wn = turtle.Screen()
wn.bgcolor("light green")

phillip = turtle.Turtle()
phillip.color("hot pink")
phillip.speed(4)

phillip.penup()
phillip.backward(200)
phillip.pendown()

drawMultipleStars(phillip, 50, 5)

wn.exitonclick()