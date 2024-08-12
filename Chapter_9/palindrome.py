#A Function that recognizes if a word is a palindrome

print("This is a program that tests to see if a word is a palindrome.")

def reversed_str(forward_str):
    reversed_str = ""
    for letter in forward_str:
        reversed_str = letter + reversed_str
    
    return reversed_str
    
def is_palindrome(str):    
	str = str.lower()
	if str == reversed_str(str):
		return True
	else:
		return False


input_str = str(input("Please input a string to test: "))

print(is_palindrome(input_str))
