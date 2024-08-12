#A program that tells is a number is odd by using a not operator

def is_even(number):
    return(number % 2 == 0)

def is_odd(number):
    test_number = not is_even(number)
    print(test_number)

to_test = int(input('Enter a number. The program will return "True" if it is even and ' \
    '"False" if it is not. '))

is_odd(to_test)