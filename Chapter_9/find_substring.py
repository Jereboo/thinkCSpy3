"""Task: Write a function that removes the first occurrence of a string from another 
string."""

#A program that removes the first occurrence of string from another string

pre_test_variable = "Hello world"
test_variable = pre_test_variable.lower() #preps the variable for the loop

#a fx that finds and returns the indexes of every occurrence of a substring within a string
def find_str(word, str):
	current_iteration = 0
	idxs = []
	while current_iteration < len(word):
		if word[current_iteration] == str:
			idxs.append(current_iteration)
			current_iteration += 1
		else:
			current_iteration += 1
	
	return idxs

initial_word = input("Please enter the string you want to use: ")
to_input_word = initial_word.lower()

initial_str = input("What substring do you want to search for: ")
to_input_str = initial_str.lower()

print(find_str(to_input_word, to_input_str))

