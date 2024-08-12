"""
3 Laws of Recursion:
1. Base Case
2. Recursive Call
3. Alteration towards base case at each recursive call

-----------------------
Modify the recursive tree program using one or all of the following ideas:

    Modify the thickness of the branches so that as the branchLen gets smaller, the line
    gets thinner.
    Modify the color of the branches so that as the branchLen gets very short it is 
    colored like a leaf.
    Modify the angle used in turning the turtle so that at each branch point the angle is
    selected at random in some range. For example choose the angle between 15 and 45 
    degrees. Play around to see what looks good.
    Modify the branchLen recursively so that instead of always subtracting the same 
    amount you subtract a random amount in some range.

If you implement all of the above ideas you will have a very realistic looking tree.
"""

#I FREAKING FIGURED IT OUT HOW TO ADJUST THE COLORS!!!! (I still have no idea how the flow of execution works though)

import turtle
import random

def tree(branchLen,t):
    if branchLen > 5:
        t.pendown()
        if branchLen > 20:
        	t.color("brown")
        t.pensize(branchLen/15)
        #t.pendown()<--color
        t.forward(branchLen)
        angle = random.randrange(15, 45)
        t.right(angle)
        tree(branchLen-random.randrange(7,15), t)
        t.pensize(branchLen/15)
        t.left(angle * 2)
        tree(branchLen-random.randrange(7,15),t)
        t.pensize(branchLen/15)
        t.right(angle)
        if branchLen < 15:
        	t.color("green")
        t.backward(branchLen)
        t.penup()
        

def main():
	t = turtle.Turtle()
	myWin = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.speed(10)
	t.color("brown")
	t.pensize(7)
	tree(75, t)
	myWin.exitonclick()

main()

"""
#Original recursive tree program from lesson
import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()
"""