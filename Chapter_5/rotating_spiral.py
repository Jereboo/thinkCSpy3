import turtle

def spiralSquare(t, sz, sq):
    for i in range(int(sq)):
        t.right(90)
        t.forward(sz)
        sz = sz * 2

wn = turtle.Screen()
wn.bgcolor("light green")

alex = turtle.Turtle()
alex.color("blue")

spiralSquare(alex, 1, 23)

wn.exitonclick()