"""
Write a program that allows the user to enter a string. It then prints a table of the 
letters of the alphabet in alphabetical order which occur in the string together with the
number of times each letter occurs. Case should be ignored. A sample run of the program
might look this this: 

Please enter a sentence: ThiS is String with Upper and lower case Letters.
a  2
c  1
d  1
e  5
g  1
h  2
i  4
l  2
n  2
o  1
p  2
r  4
s  5
t  5
u  1
w  2
$
"""

"""First Attempt: 
for word in lst_of_str:
    for ch in word:
    	letter_dict[ch] = ''
    	if letter_dict[ch] == '':
    		letter_dict[ch] = 1
    	else:
    		letter_dict[ch] = letter_dict[ch] + 1
    	print(letter_dict[ch])
    print(letter_dict)
print(letter_dict)
"""

"""Testing before wrapping into a function:
user_str = "This is a test sentence. Let's see if this works."
lower_str = user_str.lower()
print(lower_str)

lst_of_str = user_str.split(' ')
print(lst_of_str)

letter_dict = {}

for ch in "abcdefghijklmnopqrstuvwxyz":
    letter_dict[ch] = 0

for word in lst_of_str:
    for ch in word:
        if ch.isalpha():
        	lower_ch = ch.lower()
        	letter_dict[lower_ch] = letter_dict[lower_ch] + 1

for key in letter_dict:
    if letter_dict[key] != 0:
    	print(key, letter_dict[key])
"""

def letter_count(str):
    lower_str = str.lower()
    lst_of_str = lower_str.split(' ')
    letter_dict = {}
    for ch in "abcdefghijklmnopqrstuvwxyz": #establishes a dictionary w/ all letters set to 0
        letter_dict[ch] = 0
    for word in lst_of_str:
    	for ch in word:
    		if ch.isalpha():
    			letter_dict[ch] = letter_dict[ch] + 1
    for key in letter_dict:
    	if letter_dict[key] != 0:
    		print(key, letter_dict[key])

user_input = input("Please input a sentence and we will count how many of each letter it has in it!\nInput Sentence: ")

letter_count(user_input)
