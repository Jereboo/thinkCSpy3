"""
Write a recursive function to compute the factorial of a number.
  
Factorial Definition: https://en.wikipedia.org/wiki/Factorial  
In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product
of all positive integers less than or equal to n. For example:
	5! = 5x4x3x2x1 = 120
The value of 0! is 1, according to the convention for an empty product.

3 laws of recursion:
1. Base case
2. Recursive call
3. Alteration at each call to work towards base case
"""

def factorial(num):
	if num == 0:
		return 1
	elif num < 0:
		return "Error: Enter a number greater than or equal to 0."
	elif num == 1:
		return num
	return factorial(num-1) * num

test_num = int(input("Please enter a number to get its factorial: ")) 

print(factorial(test_num))
