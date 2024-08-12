#A program to manually calculate a square root using Newton's algorithm

def my_sqrt(n):
    guess = n/2
    for i in range(n):
        guess = (1/2)*(guess + (n/guess))
           
    return guess
    
to_sqrt = int(input("Please enter a number to find the square root of: "))
sqrt_estim = my_sqrt(to_sqrt)

print("The approximate square root of", to_sqrt, "is:", sqrt_estim)