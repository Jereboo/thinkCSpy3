"""At the bottom of this page is a very long file called mystery.txt The lines of this 
file contain either the word UP or DOWN or a pair of numbers. UP and DOWN are instructions
for a turtle to lift up or put down its tail. The pairs of numbers are some x,y 
coordinates. Write a program that reads the file mystery.txt and uses the turtle to draw 
the picture described by the commands and the set of points."""

import turtle

window = turtle.Screen()

fred = turtle.Turtle()
fred.shape("turtle")
fred.speed(5)

#test and refresher of turtle movement
"""
fred.up()
fred.goto(-218, 185)
fred.down()
fred.goto(-240, 189)
fred.goto(-246, 188)
fred.goto(-248, 183)
""" 

#opens mystery.txt and creates a list with each line
mystery_file = open("mystery.txt", "r")
mystery_line = mystery_file.readline()
while mystery_line:
    values = mystery_line.split()
    if values[0] == "UP":
        fred.up()
        #print("fred is up") #print line to test conditional
    elif values[0] == "DOWN":
        fred.down()
        #print("fred is down") #print line to test conditional
    else:
        #print(values) #print line to test conditional
        fred.goto(int(values[0]), int(values[1]))
    mystery_line = mystery_file.readline()

#mystery_lst = mystery_file.readlines() <--- beginning of my original code, but tried their template from other, unrelated problem for processing and splitting lines

mystery_file.close()

print("IT'S A GODDAMN BRONTASAURUS!")

window.exitonclick()