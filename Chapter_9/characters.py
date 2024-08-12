"""----------------
Task: Assign to a variable in your program a triple-quoted string that contains your 
favorite paragraph of text - perhaps a poem, a speech, instructions to bake a cake, some 
inspirational verses, etc.

Write a function that counts the number of alphabetic characters (a through z, or A 
through Z) in your text and then keeps track of how many are the letter ‘e’. 
Your function should print an analysis of the text like this:

Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'.

-------------------"""

import string

def total_letter_count(sentence):
#Counts the total number of letters in a given string
	total_count = 0
	for letter in sentence:
		if letter in string.ascii_lowercase or letter in string.ascii_uppercase:
			total_count += 1
	return total_count
	

def letter_count(letter, sentence):
	total_letter_count(sentence)
	letter_count = 0
	for letter in sentence:
		if letter == "e":
			letter_count += 1
	return letter_count


def main(): 
	#Creates a variable containing one of my favorite quotes
	LOTR_sentence = ('"Do not be afraid", said Aragorn... "His grief he will not forget;' 
					'but it will not darken his heart, it will teach him wisdom."') #93
	
	#Creates another optional variable containing one of my favorite quotes
	Evey_sentence = ("Don\'t run from it, Evey. This may be the most important moment of "
					"your life. Commit to it.")
	
	total_count = total_letter_count(LOTR_sentence)
	
	given_letter_count = letter_count("e", LOTR_sentence)
	
	#Calculates the percentage of a given letter in a given text
	letter_percent = given_letter_count / total_count * 10000 // 1 / 100 #rounds the percentage to 2 decimals
	letter_per_str = "(" + str(letter_percent) + ")"
	
	print()
	print(LOTR_sentence)
	print()
	print('Your text contains', total_count, 'alphabetic characters, of which', \
	given_letter_count, letter_per_str, 'are "e".')
	print()


main()
