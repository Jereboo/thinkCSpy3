"""
Write a function that takes a string as a parameter and returns a new string that is the
reverse of the old string.
"""

def reverse_str(str):
	"""
	recursive_counter = 0 <--- Tried to count times it was recursively called by an
		accumulator, but couldn't as this local variable would reset to 0 with each recursive
		call would need a global counter to truly count?
	"""
	if len(str) == 1:
		return str[0]
	else:
		"""
		#See above^
		recursive_counter += 1
		print("This function has been called recursively:", recursive_counter, "times.")
		"""
		return reverse_str(str[1:]) + str[0]

test_str = input("Please enter a string to be reversed: \n")

print(reverse_str(test_str))