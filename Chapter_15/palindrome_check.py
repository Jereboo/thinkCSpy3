"""
Write a function that takes a string as a parameter and returns True if the string is a 
palindrome, False otherwise. Remember that a string is a palindrome if it is spelled the
same both forward and backward. for example: radar is a palindrome. for bonus points 
palindromes can also be phrases, but you need to remove the spaces and punctuation before 
checking. for example: madam i’m adam is a palindrome. 
Other fun palindromes include:

    kayak
    boiiob
    aibohphobia
    Live not on evil
    Reviled did I live, said I, as evil I did deliver
    Go hang a salami; I’m a lasagna hog.
    Able was I ere I saw Elba
    Kanakanak – a town in Alaska
    Wassamassaw – a town in South Dakota
"""

#I FUCKING DID IT!!! FUCK YEAH!!! BOOYEAHHHHHHHHH!!!
#Only works on single words, not on phrases or things with punctuation
#Probably need to make a translation table to make it work
def palindrome_check(str):
	#lower_str = str.lower()
	#print(lower_str)
	if str[0] == str[-1]:
		if len(str) > 2:
			return palindrome_check(str[1:-1])
		else:
			return True	
	
	else:
		return False

"""
SCRATCH WORK:	
---------------
First attempt: <--- Didn't work as it just checked two middlest str characters and not entire str- DUH!
def palindrome_check(str):
	if len(str) % 2 == 0: #Evens
		if str[len(str)//2] == str[len(str)//2 - 1]:
			return True	
		else:
			return False	
	else: #Odds
		if str[len(str)//2 + 1] == str[len(str)//2 - 1]:
			return True
		else:
			return False
---------------
Other idea:
	if org_str == rev_str:
		Return True
	else:
		Return False
---------------
Revere_string function:
def palindrome_check(str):
	if len(str) == 1:
		return str[0]
	else:
		return palindrome_check(str[1:]) + str [0]
"""

input_str = input("Please input a word/phrase to see if it is a palindrome: \n")

print(palindrome_check(input_str))