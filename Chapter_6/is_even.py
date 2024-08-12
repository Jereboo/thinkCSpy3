#A program that tells is a number is even

def is_even(number):
    print(number % 2 == 0)

to_test = int(input('Enter a number. The program will return "True" if it is even and ' \
    '"False" if it is not. '))

is_even(to_test)