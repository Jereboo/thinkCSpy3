#A program to draw a simple 5 pointed star w/ a length of 100 for each side
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