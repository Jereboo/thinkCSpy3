"""
3 Laws of recursion
1. Base Case
2. Recursive call
3. Alteration on each iteration towards base case.

Write a recursive function to compute the Fibonacci sequence. How does the performance
of the recursive function compare to that of an iterative version? 


Fibonacci Sequence: Fn = Fn − 1 + Fn − 2
Seed values:
	F1 = 1, F2 = 1
or
    F0 = 0 , F1 = 1

"""

def fibonacci(iterations):
	if iterations <= 1:
		return iterations
	return  fibonacci(iterations - 1) + fibonacci(iterations - 2)  

"""
#Had to find solution via google. Tried to figure out via making a list, but this was much simpler.
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
"""

test_num = int(input("Please enter a number to get the fibonacci sequence for that number: \n"))

print(fibonacci(test_num))