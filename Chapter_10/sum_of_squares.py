"""Write a function sum_of_squares(xs) that computes the sum of the squares of the 
numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 
which is 29: """

import random
import time #<--- Sets you up to see how fast your fx processes

lst = []

for number in range(10):
    lst.append(random.randrange(-10, 11))

#print(lst)

def sum_of_squares(xs):
    total = 0
    for number in xs:
        total += number ** 2
    
    return total

print("The sum of each of these numbers squared is:", sum_of_squares(lst))


"""Write a function to count how many odd numbers are in a list."""
def count_odd(xs):
	count = 0
	for number in xs:
		if number % 2 != 0:
			count += 1
	
	return count

print("The total number of odds is:", count_odd(lst))


"""Sum up all the even numbers in a list. """
def total_of_evens(xs):
	total_even = 0
	for number in xs:
		if number % 2 == 0:
			total_even += number
	return total_even
	
	
print("Total of the evens:", total_of_evens(lst))


"""Sum up all the negative numbers in a list."""

total = 0
for number in lst:
    if number < 0:
        total += number

print("The total of all the negative numbers is:", total)


"""Sum all the elements in a list up to but not including the first even number."""
def odds_until_even(xs):
	count = 0
	total = 0
	for number in lst:
		if number % 2 != 0:
			total += number
			count += 1
		else:
			if count != 0:
				print("The total of the odds until the first even is:", total)
				break
			if count == 0:
				print("The first number in the list was an even.")
				break
	
	
def their_sum(lst):
    sum = 0
    index = 0
    while index < len(lst) and lst[index] % 2 != 0:
        sum = sum + lst[index]
        index = index + 1
    return sum

start_time = time.clock() #<--- Let's you see how fast it processes: Log's current time
odds_until_even(lst)
print("My function takes:", time.clock() - start_time, "seconds") #<--- Let's you see how fast it processes: calculates time of fx exec.

start_time = time.clock() #<--- Let's you see how fast it processes: Log's current time
their_sum(lst)
print("The original function takes:", time.clock() - start_time, "seconds") #<--- Let's you see how fast it processes: calculates time of fx exec.