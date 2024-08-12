"""
Here’s a table of English to Pirate translations
English 	Pirate
sir 	matey
hotel 	fleabag inn
student 	swabbie
boy 	matey
madam 	proud beauty
professor 	foul blaggart
restaurant 	galley
your 	yer
excuse 	arr
students 	swabbies
are 	be
lawyer 	foul blaggart
the 	th’
restroom 	head
my 	me
hello 	avast
is 	be
man 	matey

Write a program that asks the user for a sentence in English and then translates that 
sentence to Pirate.
"""

pirate_dict = {}
pirate_dict['sir'] = 'matey'
pirate_dict['hotel'] = 'fleabag inn'
pirate_dict['student'] = 'swabbie'
pirate_dict['boy'] = 'matey'
pirate_dict['madam'] = 'proud beauty'
pirate_dict['professor'] = 'foul blaggart'
pirate_dict['restaurant'] =	'galley'
pirate_dict['your'] = 'yer'
pirate_dict['excuse'] = 'arr'
pirate_dict['students'] = 'swabbies'
pirate_dict['are'] = 'be'
pirate_dict['lawyer'] = 'foul blaggart'
pirate_dict['the'] = "th'"
pirate_dict['restroom'] = 'head'
pirate_dict['my'] = 'me'
pirate_dict['hello'] = 'avast'
pirate_dict['is'] = 'be'
pirate_dict['man'] = 'matey'

eng_sent = input('Please type a sentence to be translate to pirate: ')
words_in_sent = eng_sent.lower().split()
new_sentence_words = []

for word in words_in_sent:
    if word in pirate_dict:
        new_sentence_words.append(pirate_dict[word])
    else:
    	new_sentence_words.append(word)

pirate_sentence = ''

for word in new_sentence_words:
	pirate_sentence = pirate_sentence + word + ' '	

print(pirate_sentence)