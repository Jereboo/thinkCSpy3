#A program to draw a series of rotating squares
import turtle

def drawISquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawIISquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.backward(sz)
        t.left(90)  

def drawIIISquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.backward(sz)
        t.right(90)   
       
def drawIVSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.right(90) 

def drawBigSquare(t, sz):
    drawISquare(t, sz)
    drawIISquare(t, sz)
    drawIIISquare(t, sz)
    drawIVSquare(t, sz)
    

def drawRotatingSquares(t, sz, sq):
    for i in range(int(sq)):
        drawBigSquare(t, sz)
        t.left(360/sq)
        
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")
alex.width(2)
alex.speed(10)

drawRotatingSquares(alex, 100, 10)

wn.exitonclick()