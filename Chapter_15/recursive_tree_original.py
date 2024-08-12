#Original recursive tree program from lesson

import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.pendown()
        if branchLen > 20:
        	t.color("brown")
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        if branchLen < 20:
        	t.color("green")
        t.backward(branchLen)
        t.penup()

def main():
    t = turtle.Turtle()
    t.speed(1)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.pensize(1)
    tree(60,t)
    myWin.exitonclick()

main()