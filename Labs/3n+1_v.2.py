"""
Repeat the call to seq3np1 using a range of values, up to and including an upper bound.

Now that we have a function that can return the number of iterations required to get to 1,
we can use it to check a wide range of starting values. In fact, instead of just doing one
value at a time, we can call the function iteratively, each time passing in a new value.

Create a simple for loop using a loop variable called start that provides values from 1 up
to 50. Call the seq3np1 function once for each value of start. Modify the print statement
to also print the value of start.


For further tips visit: http://interactivepython.org/runestone/static/thinkcspy/Labs/sequencelab.html
"""

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

start = range(1,51)

for i in start:
	print("Iterations for", i, "=", seq3np1(i))

#print(seq3np1(3))

