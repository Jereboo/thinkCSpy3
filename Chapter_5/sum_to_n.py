#A Program that returns the sum of integers up to and including n

def sumTo(n):
    result = (n * (n + 1)) / 2
    return result

number = int(input("Please enter a number to add the previous integers of: "))
total = sumTo(number)   

print("If you add every integer up to and including", number, "the answer is: ", total)