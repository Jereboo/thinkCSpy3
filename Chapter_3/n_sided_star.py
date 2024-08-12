#A program to draw a n sided star

import turtle

def drawStar(t, sz, pts):
    for i in range(pts):
        t.forward(sz)
        t.right(pts/(225/36))

wn = turtle.Screen()
wn.bgcolor("light green")

phillip = turtle.Turtle()
phillip.color("hot pink")
phillip.speed(1)

drawStar(phillip, 50, 5)

wn.exitonclick()