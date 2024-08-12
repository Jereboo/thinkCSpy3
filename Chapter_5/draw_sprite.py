#A program that draws a sprite w/ "num" of legs that are "length" long.
import turtle

def draw_sprite(t, num, length): #needs turtle, number of legs, & length of legs
    for i in range(4):
        t.forward(10 * (num-1))
        t.left(90)
            
    for i in range(int(num)):
        t.right(90)
        t.forward(length)
        t.penup()
        t.home()
        t.forward((i+1)*10)
        t.pendown()
    t.penup()
    t.home()
    t.pendown()    

wn = turtle.Screen()
wn.bgcolor("green")

bill = turtle.Turtle()
bill.color("blue")
bill.speed(10)

draw_sprite(bill, 7, 50)

wn.exitonclick()