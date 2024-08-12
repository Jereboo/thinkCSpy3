"""
Create a list containing 100 random integers between 0 and 1000 (use iteration, append, 
and the random module). Write a function called average that will take the list as 
a parameter and return the average.
"""

#I wrote my fx for to find a max number in a list, which is 4x slower than the solution

import random
import time #<--- Sets you up to see how fast your fx processes

#creates a list with 100 random int.s btw 0-1000
my_list = []
for number in range(1000):
    my_list.append(random.randrange(1001))

#finds the average of a list of int.s
#inputs (list, #_in_list)
def average(lst_of_numbers):
    sum_of_list = 0
    for item in lst_of_numbers:
        sum_of_list += item
    avg_of_list = sum_of_list/len(lst_of_numbers)
    return avg_of_list

print("The average of all of these values is:", average(my_list))

def max(lst_of_numbers):
    """lst_of_numbers.sort()
    return lst_of_numbers[-1]""" #<--- Easy way out
    max_value = 0 		#Sets a counter for max_value
    for i in range(len(lst_of_numbers)// 2): #Divides the list in two to negate unnecessary loops
        if lst_of_numbers[i] >= lst_of_numbers[-1 * i]:  #Sees if lower extreme of list is >= to higher extreme of list
            if lst_of_numbers[i] >= max_value:   #if is >= then compares to current max_value and stores if >=
                max_value = lst_of_numbers[i]
        else:
            if lst_of_numbers[-1 * i] >= max_value: #if higher extreme is >= then compares to current max_value and stores if >=
        	    max_value = lst_of_numbers[-1 * i]
            
    return max_value
    
def their_max(lst):
    max = 0
    for e in lst:
        if e > max:
            max = e
    return max
 
start_time = time.clock() #<--- Let's you see how fast it processes: Log's current time

print("The maximum value is:", max(my_list))
print("My function takes:", time.clock() - start_time, "seconds") #<--- Let's you see how fast it processes: calculates time of fx exec.

start_time = time.clock() #<--- Let's you see how fast it processes: Log's current time
their_max(my_list)
print("The original function takes:", time.clock() - start_time, "seconds") #<--- Let's you see how fast it processes: calculates time of fx exec.


#my_list.sort()
#print(my_list)