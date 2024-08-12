"""
Although Python provides us with many list methods, it is good practice and very 
instructive to think about how they are implemented. Implement a Python function that
works like the following:
    count
    in
    reverse
    index
    insert
"""

import random
#import time #<--- Sets you up to see how fast your fx processes

lst = []

for number in range(10):
    lst.append(random.randrange(-10, 11))

print(lst)

#count
def my_count(item_to_count, lst):
    count = 0
    int_of_item = int(item_to_count)
    for item in lst:
        if item == int_of_item:
            count += 1
            
    return count


test_count = input("What item do you want to count? ")

print("The total number of", test_count + "s", "in this list is", my_count(test_count, lst))


#in
def my_is_in(orig_lst, to_find):
	for position in range(len(orig_lst)):
		if orig_lst[position] == to_find:
			#print("Found it!") #Test print for debugging
			return True
		
	return False

to_see_if_in = int(input("Input a number to see if it is in the list: "))

print("Is", to_see_if_in, "in the original list?", my_is_in(lst, to_see_if_in))
	
"""Test code prior to generalizing and wrapping into a fx
test_lst = [10, 7, 4, 3, 5, 7, 1]
to_find = 1

for position in range(len(test_lst)):
	if test_lst[position] == to_find:
		print(True)
		break
	
	print(False) #incorrect before generalization- prints False each loop
	#return False"""


#reverse
def my_reverse(orig_lst):
	new_lst = []
	for position in range(1, len(orig_lst) + 1):
		#print(position * -1)
		new_lst.append(lst[position * -1])
		#print(new_lst)
	
	return new_lst


print("The original list is:\n", lst, "\nThe original list reversed is:\n", my_reverse (lst))

#index
def my_index(orig_lst, item_to_find):
	current_iteration = 0
	for item in orig_lst:
		if item == item_to_find:
		    break
		current_iteration += 1
		
	return current_iteration

to_find = int(input("What item do you want to find the index of? "))

print("The index of", to_find, "is:", my_index(lst, to_find))

"""Test code prior to generalizing and wrapping into a fx
test_lst = [10, 7, 4, 3, 5, 7, 1]

current_iteration = 0
for item in test_lst:
	if item == 1:
	    break
	current_iteration += 1

print(current_iteration)"""
	

#insert
def my_insert(orig_lst, insert_index, item_to_insert):
	new_lst = []
	for position in range(len(orig_lst) + 1):
		if position < insert_index:
			new_lst.append(orig_lst[position])
		elif position == insert_index:
			new_lst.append(item_to_insert)
		elif position > insert_index:
			new_lst.append(orig_lst[position - 1])
	
	return new_lst
	
	
insert_index = int(input("At what index do you want to insert the number? "))
to_insert = int(input("What number do you want to insert into the list? "))
lst_after_insert = my_insert(lst, insert_index, to_insert)

print("The original list was:\n", lst, "\nThe new list after inserting", to_insert, "is:\n", lst_after_insert)

"""Test code prior to generalizing and wrapping into a fx
test_lst = [10, 7, 4, 3, 5, 7, 1]
to_insert = 6
insert_index = 3

new_lst = []
for position in range(len(test_lst) + 1):
    if position < 3:
        new_lst.append(test_lst[position])
    elif position == 3:
        new_lst.append(to_insert)
    elif position > 3:
        new_lst.append(test_lst[position - 1])

print(new_lst)"""



