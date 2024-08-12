import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.left(90)

def drawFourSquares(t,sz): #Draws the bigger square that is the basis of the larger polygon
    for i in range(4):
        drawSquare(t,sz)

def drawRotatingSquares(t, sz, sq): #sq==number of squares in the larger polygon 
    for i in range(int(sq)): #more squares will decrease white space; less squares with increase white space
        drawFourSquares(t, sz)
        t.left(360/sq) #360/sq to make the shape uniform across a 360 degree circle
        

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")
alex.width(2)
alex.speed(0)

drawRotatingSquares(alex, 30, 6) #when sq== 4 or 8 it does not produce a shape b/c sq == 90

wn.exitonclick()