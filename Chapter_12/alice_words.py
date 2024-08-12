"""
Write a program called alice_words.py that creates a text file named alice_words.txt 
containing an alphabetical listing of all the words, and the number of times each occurs,
in the text version of Alice’s Adventures in Wonderland. (You can obtain a free plain 
text version of the book, along with many others, from http://www.gutenberg.org.) 
The first 10 lines of your output file should look something like this:

    Word 	Count
    a 	631
    a-piece 	1
    abide 	1
    able 	1
    about 	94
    above 	3
    absence 	1
    absurd 	2

How many times does the word, alice, occur in the book? If you are writing this in the 
activecode window simply print out the results rather than write them to a file.
"""

"""To do:
-making all words lowercase to avoid duplicates (x)
-removing punctuation (x)
-sorting the dictionary (x)
-Formatting the output (x)
-writing the output to a file
"""

"""
Note: Program still a little buggy, even with their solution
"""

all_words = {}

source_file = open('alice_in_wonderland.txt', 'r')
out_file = open('alice_words.txt', 'w')

line = source_file.readline()
while line:
    words_in_line = line.split()
    for word in words_in_line:
        word = word.lower()
        word = word.replace('`', '').replace('~', '').replace('!', '').replace('@', '')
        word = word.replace('#', '').replace('$', '').replace('%', '').replace('^', '')
        word = word.replace('&', '').replace('*', '').replace('(', '').replace(')', '')
        word = word.replace('-', '').replace('_', '').replace('=', '').replace('+', '')
        word = word.replace('[', '').replace('{', '').replace(']', '').replace('}', '')
        word = word.replace('\\', '').replace('|', '').replace(';', '').replace(':', '')
        word = word.replace("'", '').replace('"', '').replace(',', '').replace('<', '')
        word = word.replace('.', '').replace('>', '').replace('/', '').replace('?', '')
        word = word.replace(' ', '').replace('\n', '')
        #lower_word = word.lower() <---I forgot I do not need a new variable name each time
        #stripped_word = lower_word.strip('`~!@#$%^&*()-_=+[{]}|;:",<.>/\\\'\n ') <-- My solution for removing punctuation- several '\'s to allow for all punctuations w/o escaping quotes- still buggy and does not remove all punctuation
        #stripped_word = stripped_word_round_1.strip("'\\")
        if word in all_words:
            all_words[word] = all_words[word] + 1
        else:
            all_words[word] = 1
    line = source_file.readline()


words_to_sort = all_words.keys()
for word in sorted(words_to_sort):
    #print(word, all_words[word]) #<-- For testing purposes in shell
    out_file.write(word + ' ' + str(all_words[word]) + '\n')

#print(all_words) <-- For testing in shell

source_file.close() #is placing at end better style?
out_file.close()