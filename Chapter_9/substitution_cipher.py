"""----
Task: Write a function that implements a substitution cipher. In a substitution cipher 
one letter is substituted for another to garble the message. For example A -> Q, B -> T,
C -> G etc. your function should take two parameters, the message you want to encrypt, 
and a string that represents the mapping of the 26 letters in the alphabet. Your function 
should return a string that is the encrypted version of the message.
----"""

#A program that codes a message using a substitution cipher

import string
import random

def random_letter_coding(): #a function that creates a random letter coding map
    alphabet_mapping = "abcdefghijklmnopqrstuvwxyz"
    random_letter = random.randrange(0, 26)
    new_alphabet_mapping = ""
    for letter in alphabet_mapping:
        new_random_index = random.randrange(0,26)
        new_random_letter = alphabet_mapping[new_random_index]
        while new_random_letter in new_alphabet_mapping:
            new_random_index = random.randrange(0,26)
            new_random_letter = alphabet_mapping[new_random_index]
        else:
            new_alphabet_mapping += new_random_letter
    
    return new_alphabet_mapping
    
def random_letter_key(mapping_key_var): #for debugging- a function that produces a nice, visual key based on the random letter coding map
    print("The key is:", mapping_key_var)
    print("Here is a nice, pretty version of the key (Original letter > Encrypted letter):") #Is there are an easy way to flip this around?
    alphabet_mapping = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for letter in alphabet_mapping:
        print(letter, "=", mapping_key_var[count])
        count += 1

def message_encryption(message):
    alphabet_mapping = "abcdefghijklmnopqrstuvwxyz"
    random_letter_mapping_code = random_letter_coding()
    random_letter_code_key = random_letter_key(random_letter_mapping_code)
    print(random_letter_code_key)
    encrypted_message = ""
    current_iteration = 0
    for letter in message:
        count = 0
        if letter in string.ascii_lowercase: #current problem moving to else statement with spaces
    	    while letter != alphabet_mapping[count]: #"e" = indx. 4
        	    count += 1
    	    else:
        	    encrypted_message += random_letter_mapping_code[count]
        	    current_iteration += 1
        	    #print("The encrypted message so far is:", encrypted_message)
        else:
    	    encrypted_message += letter
    	    #print("The encrypted message so far is:", encrypted_message)

    return encrypted_message


original_message = input("Please enter a message to encrypt: ")
to_input_message = original_message.lower()

final_encrypted_message = message_encryption(to_input_message)

print(original_message, "encrypted is:", final_encrypted_message) 	

"""------------------------------------------
Their significantly more elegant solution:

def encrypt(message, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ''
    for char in message:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            pos = alphabet.index(char)
            encrypted = encrypted + cipher[pos]
    return encrypted

def decrypt(encrypted, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ''
    for char in encrypted:
        if char == ' ':
            decrypted = decrypted + ' '
        else:
            pos = cipher.index(char)
            decrypted = decrypted + alphabet[pos]
    return decrypted


cipher = "badcfehgjilknmporqtsvuxwzy"

encrypted = encrypt('hello world', cipher)
print encrypted

decrypted = decrypt(encrypted, cipher)
print(decrypted)

----------------------------------------------------"""


        
	