"""
3 Laws of Recursion:
1. Base Case
2. Recursive Call
3. Adjustment at each call towards base case

Find or invent an algorithm for drawing a fractal mountain. Hint: One approach to this 
uses triangles again.
"""
#Adapted from Sierpinski's Triangle program from lesson

import turtle
import random

def drawTriangle(points, myTurtle):
	myTurtle.up()
	myTurtle.goto(points[0][0], points[0][1])
	myTurtle.down()
	myTurtle.goto(points[1][0], points[1][1])
	myTurtle.goto(points[2][0], points[2][1])
	myTurtle.goto(points[0][0], points[0][1])

def getMid(p1, p2):
	return ((p1[0]+p2[0])/2, (p1[1] + p2[1])/2) #<--- Random element needed here?

def fractal_mountain(points, degree, myTurtle):
	drawTriangle(points, myTurtle)
	#random_point = random.randrange() #<--- Got stuck here, realized how complicated it would be to find random point in the area of the triangle.
	#drawTriangle([[-50,25], [50, 25], [0, -50]], myTurtle) <---midpoints
	if degree > 0:
		fractal_mountain([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)
		fractal_mountain([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree-1, myTurtle)
		fractal_mountain([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)

def main():
	myTurtle = turtle.Turtle()
	myWin = turtle.Screen()
	myPoints = [[-100,-50],[0,100],[100,-50]]
	fractal_mountain(myPoints, 3, myTurtle)
	myWin.exitonclick()


main()

"""Sierpinski Triangle program from lesson:
import turtle

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

main()
"""