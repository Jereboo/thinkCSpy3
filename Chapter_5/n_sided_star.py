#A program to draw a n sided star

import turtle

def drawStar(t, sz, pts):
    for i in range(pts):
        t.forward(sz)
        t.right(180 - 180/pts)

wn = turtle.Screen()
wn.bgcolor("light green")

phillip = turtle.Turtle()
phillip.color("hot pink")
phillip.speed(4)

drawStar(phillip, 100, 9)

wn.exitonclick()