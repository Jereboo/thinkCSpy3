#A function that reverses a string

def reversed_str(forward_str):
    reversed_str = ""
    for letter in forward_str:
        reversed_str = letter + reversed_str
    
    return reversed_str

input_str = str(input("Please type in a string you want reversed: "))

print(reversed_str(input_str))