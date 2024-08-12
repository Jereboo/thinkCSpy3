"""
Count the number of iterations it takes to stop.

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
    return count                  # the last print is 1

print(seq3np1(3))

