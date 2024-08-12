"""
Now we can put the two previous programs together to complete our plot. Here is our
sequence of steps.

    Create and set up the turtle and the screen.

    Iterate the angle from 0 to 360.

            Generate the sine value for each angle.
            Move the turtle to that position (leave a line behind).

Here is a partial program for you to complete.
"""

import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setworldcoordinates(-1,-2 , 400,2) 

fred = turtle.Turtle()
fred.write(0)
fred.goto(0, -1)
fred.write(-1)
for degree in range(0, 361, 30):
	fred.goto(degree, -1)
	fred.write(degree) 
fred.goto(360, -1)
fred.goto(0,-1)
fred.goto(0,1)
fred.write(1)


for angle in range(1, 361):
	print(math.sin(math.radians(angle)))
	fred.goto(angle, math.sin(math.radians(angle)))

wn.exitonclick()
