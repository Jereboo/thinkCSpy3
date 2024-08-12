"""
What is the longest word in Alice in Wonderland? How many characters does it have?
"""

"""To address:
Find way to sort by value
"""


in_file = open('alice_words.txt', 'r')

all_words = {}

line = in_file.readline()
while line:
	line = line.lower().split()
	for word in line:
		if word.isalpha():
			ch_count = 0
			for ch in word:
				ch_count += 1
			all_words[word] = ch_count
	line = in_file.readline()           

all_words_values = all_words.values()
all_words_values = sorted(all_words_values, reverse=True) #Stopped at this point. Got very tired.


all_words_keys = all_words.keys()
all_words_keys = sorted(all_words_keys, key=all_words.get, reverse=True)
#print(all_words_keys) <--for testing

print(all_words_keys[0], "is the longest word, with it being" ,all_words[all_words_keys[0]], "letters long.")

#print(all_words)
    

in_file.close()