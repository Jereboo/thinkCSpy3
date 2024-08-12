
import turtle
import math
import random

fred = turtle.Turtle()
#fred.speed(0)

wn = turtle.Screen()
wn.tracer(100)
wn.setworldcoordinates(-1,-1,1,1)

fred.up()

num_darts = 10000
inside_count= 0
for i in range(num_darts):
    randx = random.random()
    randy = random.random()
    negative_x = random.random()
    negative_y = random.random()
    if negative_x >= .5:
        randx = randx * -1
    if negative_y >= .5:
        randy = randy * -1
    fred.goto(randx, randy)
    if fred.distance(0,0)> 1:
        pass
        #fred.dot(4, "red")
    else:
    	inside_count += 1
    	#fred.dot(4, "blue")
        

pi = (inside_count/num_darts) * 4
        

print("inside_count= ", inside_count)
print("Pi= ", pi)

wn.exitonclick()