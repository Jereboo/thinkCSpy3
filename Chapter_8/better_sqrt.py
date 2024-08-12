#A program to manually calculate a square root using Newton's algorithm

def my_sqrt(n):
    guess = 0.5 * n
    better = (0.5) * (guess + n / guess)
    while better != guess:
        guess = better
        better = 0.5 * (guess + n / guess)
        print("Approx.: ", better)
           
    return guess
    
to_sqrt = int(input("Please enter a number to find the square root of: "))
sqrt_estim = my_sqrt(to_sqrt)

print("The final approximate square root of", to_sqrt, "is:", sqrt_estim)

"""
def newtonSqrt(n):
    approx = 0.5 * n
    better = 0.5 * (approx + n/approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + n/approx)
        print("Approx:", better)
    return approx


print("Final approx:", newtonSqrt(25))
"""