"""
Now we will generalize the counting problem and consider how to count the number of times
each letter appears in a given string. In order to do this we need to realize that writing
a function that returns a single integer will no longer work. Instead we will need to 
return some kind of collection that holds the counts for each character.


Here is a start to the development of the function.

    Define the function to require one parameter, the string.
    Create an empty dictionary of counts.
    Iterate through the characters of the string, one character at a time.
    
    
#Got Em! There has to be a more efficient way of building the dictinoary rather than
creating a key for each letter only to delete it later on via .pop() if key == 0 (See line 29)
"""

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
	
test_str = "hello"
test_count = count_all(test_str)

input_test = input("Enter a string to count all it's letters: \n")
input_test_count = count_all(input_test)

print("test_count: \n", test_count)
print("input_test_count: \n",input_test_count)
