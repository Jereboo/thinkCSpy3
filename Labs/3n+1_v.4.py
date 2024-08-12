"""
Keep track of the maximum number of iterations.


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

max_so_far = 0
for i in start:
	current_iteration = seq3np1(i)
	if max_so_far <= current_iteration:
		max_so_far = current_iteration
	print("Iterations for", i, "=", current_iteration)
	print("Current max iterations is", max_so_far)

print(max_so_far)

#print(seq3np1(3))

