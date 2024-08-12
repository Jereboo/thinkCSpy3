"""
Write a recursive function to reverse a list. 

3 Laws of recursion:
1. Base case
2. Recursive call
3. Alteration at each call towards base case
"""

#Had to look up solution :,( Had difficulty remembering ways to append a list

def reverse_lst(lst):
	#print(lst)
	if len(lst) == 0:
		return []
	return [lst[-1]] + reverse_lst(lst[:-1]) #<---This was really damn confusing to me at first: traces down to empty list, then adds each element to this empty list from another list one at a time.
	#Below is recursive call logic for a string
	#return reverse_lst(lst[1:]) + lst [0]
	
test_lst = [1,2,3,4,5]

print(reverse_lst(test_lst))