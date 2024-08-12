"""
Use the turtle graphics to graph the number of iterations. This provides an interesting
visual that allows you to see the relative number of iterations for each value. You will
probably want to use setworldcoordinates to make your graph an appropriate scale. You
should also use the turtle to write out the loop varable and the number of iterations if
the number of iterations is more than 100.

Line graph?
x = indep. var is current_iteration
y = dep. var is number of iterations
For further tips visit: http://interactivepython.org/runestone/static/thinkcspy/Labs/sequencelab.html
"""
import turtle as turtle

def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    return count               

start = range(1,101) 

#Establishes needed size of window
max_so_far = 0
for i in start:
	current_iteration = seq3np1(i)
	if max_so_far <= current_iteration:
		max_so_far = current_iteration

#initialize turtle
graph_turt = turtle.Turtle()
graph_win = turtle.Screen()
graph_win.setworldcoordinates(-1,-1, max_so_far + 10, max_so_far + 10) #Adjusts with max iterations

#How could I abstract the increments that it writes?
for i in range(0, max_so_far - 10, 10): #max_so_far-10 is to help keep window neat and avoid prints towards edges of window
	graph_turt.forward(10)
	graph_turt.write(i)
graph_turt.goto(0,0)
graph_turt.left(90)
for i in range(0, max_so_far - 10, 10):
	graph_turt.forward(10)
	graph_turt.write(i)
graph_turt.goto(0,0)
for i in start:
	i_iteration_total = seq3np1(i)
	graph_turt.goto(i, i_iteration_total) #(x=current iteration, y=total number of iterations for x)

graph_win.exitonclick()
