"""Task: Write a function that removes the first occurrence of a string from another 
string."""

#Functions below: finds a string, removes all occurrences of a string, removes the duplicates of a string

"""--------------------------
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
------------------------------"""


"""----------------------------
#A fx that removes a given substring from a given string
#Current limitation- only can remove one char., cannot remove mult. char.s
def remove_all_str(str, sub_str):
    current_iter = 0
    new_str = ""
    while current_iter < len(str):
        if str[current_iter] != sub_str: #Test to omit substring
            new_str += str[current_iter] #compiles new string character by character
            current_iter += 1
        else: #passes the loop on without changing the new string if the current iter. is the substring
    	    current_iter += 1
    
    return new_str


initial_str = input("Please input the string you wish to edit: ")
test_str = initial_str.lower()

initial_sub_str = input("Please input the substring you wish to edit out of the original string: ")
test_sub_str = initial_sub_str.lower()

print(remove_all_str(test_str, test_sub_str))
-------------------------------"""

#A fx that removes a given substring from a given string and creates a new string without any duplicate letters
#Current limitation- only can remove one char., cannot remove mult. char.s
def remove_dupl(str, sub_str):
    current_iter = 0
    new_str = ""
    while current_iter < len(str):
        if str[current_iter] != sub_str: #Test to omit substring
            new_str += str[current_iter] #compiles new string character by character
            current_iter += 1
        elif sub_str not in new_str:
        	new_str += str[current_iter]
        	current_iter += 1
        else: #passes the loop on without changing the new string if the current iter. is the substring
    	    current_iter += 1
    
    return new_str


initial_str = input("Please input the string you wish to edit: ")
test_str = initial_str.lower()

initial_sub_str = input("Please input the substring you wish to edit out of the original string: ")
test_sub_str = initial_sub_str.lower()

print(remove_dupl(test_str, test_sub_str))