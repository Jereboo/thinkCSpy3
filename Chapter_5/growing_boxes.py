#A turtle program that draws increasingly large boxes
import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)        
        
def drawBorderSquares(t, sz, sq):
    for i in range(int(sq)):
        size = sz*(i+1)
        drawSquare(t, size)
        t.penup()
        t.goto(-sz*(i+1)*0.5, -sz*(i+1)*0.5)
        t.pendown()

wn = turtle.Screen()
wn.bgcolor("light green")

alex = turtle.Turtle()
alex.color("pink")

drawBorderSquares(alex, int(input("How long do you want the sides? ")), int(input("How many boxes do you want? ")))

print("Done! Click anywhere on the green box to exit.")
wn.exitonclick()
