#A function that removes all instances of a given letter or character from a string

print(("This is a program that lets you remove all instances of a given letter or "
		"character from a string"))

def remove_char(str_to_edit, char_to_remove):
	str_minus_char = ""
	for char in str_to_edit:
		if char != char_to_remove:
			str_minus_char = str_minus_char + char
	return str_minus_char

input_str = str(input("Please input the string you wish to edit: "))
input_char_to_remove = str(input("Please input what letter or character you wish to remove: "))

print(remove_char(input_str, input_char_to_remove))
