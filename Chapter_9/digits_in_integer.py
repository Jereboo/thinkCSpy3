#A program that returns the number of digits in an integer

def digits_in_integer(integer):
    str_integer = str(integer)
    digits_in_integer = len(str_integer)
    return digits_in_integer

input_integer = int(input("Please input a number and this program will count the number of digits in it: "))

total_digits = digits_in_integer(input_integer)

print(total_digits)