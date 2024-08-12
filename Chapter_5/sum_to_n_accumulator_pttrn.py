#A Program that returns the sum of integers up to and including n

def sumTo(n):
    running_total = 0
    for i in range(int(n)):
        running_total = running_total + (i + 1)
    
    return running_total

number = int(input("Please enter a number to add the previous integers of: "))
total = sumTo(number)   

print("If you add every integer up to and including", number, "the answer is: ", total)