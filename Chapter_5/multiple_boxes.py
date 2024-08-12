import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawMultipleSquares(t, sz, sq):
    t.penup()
    t.goto(-int(sz)*(sq), 0)
    t.pendown()
    for i in range(int(sq)):
        drawSquare(t, sz)
        t.penup()
        t.forward(sz+sz)
        t.pendown()
    t.penup()
    t.home()
        
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("pink")

drawMultipleSquares(alex, 20, 6)

wn.exitonclick()