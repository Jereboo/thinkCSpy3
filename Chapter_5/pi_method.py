#My incorrect version is triple quoted and the correct answer is below the triple quotes
"""A program to approximate pi using Leibniz's method
def pi_approx(n):
    pi_total = 0
    for i in range(n):
        pi_total = 4 * (1 - 1/i)
        pi_total = pi_total + 1/i
        return pi_total

decimals = int(input("To how many decimal points would you like to approximate pi? "))
pi_final = pi_approx(decimals)

print("The value of pi rounded to ", decimals, "decimal points is", pi_total)"""

def myPi(iters):
    ''' Calculate an approximation of PI using the Leibniz
    approximation with iters number of iterations '''
    pi = 0
    sign = 1
    denominator = 1
    for i in range(iters):
        pi = pi + (sign/denominator)
        sign = sign * -1  # alternate positive and negative
        denominator = denominator + 2

    pi = pi * 4.0
    return pi

pi_approx = myPi(10000)
print(pi_approx)