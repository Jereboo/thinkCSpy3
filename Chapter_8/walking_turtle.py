"""Task: Modify the previous turtle walk program so that the turtle turns around when it
    hits the wall or when one turtle collides with another turtle.
    #I am having trouble figuring out how to make it turn around when it hits the wall."""
    
#A Program that makes two turtles that walks randomly within the limits of the screen

import turtle
import random #I forgot this part

wn = turtle.Screen()
wn.bgcolor("light green")

#A function placing a turtle at a random starting position
def starting_position(window, turtle):  
    #Articulates the boundaries of the screen and establishes a random x & y coord. within it
    left_bound = -(wn.window_width() / 2)
    right_bound = wn.window_width() / 2
    top_bound = wn.window_height() / 2
    bottom_bound = -(wn.window_height() / 2)
    random_x_coordinate = random.randrange(left_bound, (right_bound + 1))
    random_y_coordinate = random.randrange(bottom_bound, (top_bound + 1))
    
    #Sets the turtle at a random x & y starting position
    turtle.penup()
    turtle.setx(random_x_coordinate)
    turtle.sety(random_y_coordinate)
    turtle.pendown()
	

#A Function that evaluates if the turtle is in the screen
def is_in_screen(window, turtle):
    left_bound = -(wn.window_width() / 2)
    right_bound = wn.window_width() / 2
    top_bound = wn.window_height() / 2
    bottom_bound = -(wn.window_height() / 2)
    
    turtle_x = turtle.xcor()
    turtle_y = turtle.ycor()
    
    still_in = True
    
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False
    
    return still_in
    
"""A function that determines if a turtle occupies the same space as another turtle- I am
trying to write a function that will cause the turtle to turn around if it collides with
another."""
def turtle_collision(window, turtle_1, turtle_2):
    turtle_1_position = turtle_1.position()
    turtle_2_position = turtle_2.position()
    collision = False
    if turtle_1_position == turtle_2_position:
        collision = True
        
    return collision

"""def hit_wall(wn, turtle):
    left_bound = -(wn.window_width() / 2)
    right_bound = wn.window_width() / 2
    top_bound = wn.window_height() / 2
    bottom_bound = -(wn.window_height() / 2)
    
    turtle_x = turtle.xcor()
    turtle_y = turtle.ycor()
    
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False
    
    return still_in"""

    
def random_walk(window, turtle_1, turtle_2):
    starting_position(wn, turtle_1) #Calls this function to set starting position
    starting_position(wn, turtle_2)
    while is_in_screen(window, turtle_1) or is_in_screen(window, turtle_2):
        if is_in_screen(window, turtle_1):
            turtle_1.left(random.randrange(0,361))
            turtle_1.forward(random.randrange(0,150))
            if turtle_collision(window, turtle_1, turtle_2):
                turtle_1.left(random.randrange(0,361))
                turtle_1.forward(random.randrange(0,150))
        if is_in_screen(window, turtle_2):
            turtle_2.left(random.randrange(0,361))   
            turtle_2.forward(random.randrange(0,150))
            if turtle_collision(window, turtle_1, turtle_2):
                turtle_2.left(random.randrange(0,361))
                turtle_2.forward(random.randrange(0,150))
        
        """chance = random.randrange(0, 2)
        if chance == 0:
            turtle_1.left(random.randrange(0,361))
            turtle_2.left(random.randrange(0,361))
        else:
            turtle_1.right(random.randrange(0,361)) 
            turtle_2.right(random.randrange(0,361))
        
        turtle_1.forward(random.randrange(0,100))
        turtle_2.forward(random.randrange(0,100))"""
        
        

""" # My original function
def random_walking(turtle, window_size):
    turtle_position = turtle.position()
    #screen_size = wn.screensize()
    while turtle_position < screen_size:
        random_number = random.range(0,2)
        if random_number == 0:
    	    turtle.left()
    	else:
    	    turtle.right()
    	turtle.forward(50)
    	turtle_position = turtle.position()

"""

alex = turtle.Turtle() #creates turtle_1 instance
alex.shape("turtle")
alex.color("blue")

bill = turtle.Turtle() #creates turtle_2 instance
bill.shape("turtle")
bill.color("red")

random_walk(wn, alex, bill)

wn.exitonclick()
