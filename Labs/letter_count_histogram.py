"""
The previous lab wrote a function to return a dictionary of letter counts. In an earlier
chapter, we wrote a turtle program that could draw a histogram.

Combine these two ideas together to create a function that will take a string and create a
histogram of the number of times each letter occurs. Make sure it is in alphabetical order
from left to right.

1. Count the number of times each letter occurs. Keep the count in a dictionary.
2. Get the keys from the dictionary, convert them to a list, and sort them.
3. Iterate through the keys, in alphabetical order, getting the associated value (count).
4. Make a histogram bar for each.

#Still need to work on print statement: Line 43

#Histogram lesson: interactivepython.org/runestone/static/thinkcspy/Functions/ATurtleBarChart.html
"""
import turtle

def count_all(str):
	lower_str = str.lower()
	counts = {}
	all_letters = "abcdefghijklmnopqrstuvwxyz"
	for letter in range(len(all_letters)):
		counts[all_letters[letter]] = 0
		for character in range(len(lower_str)):
			if all_letters[letter] == lower_str[character]:
				counts[all_letters[letter]] = counts[all_letters[letter]] + 1
		if counts[all_letters[letter]] == 0:
			counts.pop(all_letters[letter])
	return counts

def histogram(str):
	str_dict = count_all(str)
	hist_win = turtle.Screen()
	hist_turt = turtle.Turtle()
	hist_turt.left(90)
	for value in str_dict:
		print(value)
		hist_turt.forward(int(str_dict[value]) * 100)
		hist_turt.right(90)
		hist_turt.write(value)
		hist_turt.write("=")
		hist_turt.write()
		#hist_turt.write(value + "=" + str(str_dict[value]))
		hist_turt.forward(20)
		hist_turt.right(90)
		hist_turt.forward(int(str_dict[value]) * 100)
		hist_turt.left(180)
	hist_win.exitonclick()
	
	
test_str = "hello"
test_count = count_all(test_str)

#input_test = input("Enter a string to count all it's letters: \n")
#input_test_count = count_all(input_test)

print("test_count: \n", test_count)
#print("input_test_count: \n",input_test_count)

histogram(test_str)
#histogram(input_test)
