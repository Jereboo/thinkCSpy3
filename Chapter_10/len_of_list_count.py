"""Count how many words in a list have length 5."""

lst = ["chair", "sam", "table", "pig", "pillow", "frame"]
print(lst)

def len_of_word(lst_of_words):
	count = 0
	for word in lst_of_words:
		if len(word) == 5:
			count += 1
	return count
	
	
print(len_of_word(lst))


"""Count how many words occur in a list up to and including the first occurrence of the 
word “sam”."""


index = 0
while index <= len(lst) + 1:
	if lst[index] != "sam":
		index += 1
	else:
		index += 1
		break
		
		
print('Total number of words up to and including "sam" is', index)

    
