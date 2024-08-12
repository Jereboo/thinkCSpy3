"""A program that approximates pi using Madhava's method: 
pi == sqrt(12)(1 - 1/3*3 + 1/5*3**2 - 1/7*3**3 + ...)"""

def my_pi(n):
    pi_approx = 0
    numer = 1
    denom = 1
    pwr = 0
    for i in range(n):
	    pi_approx = pi_approx + numer/(denom * 3 ** pwr)
	    numer = numer * -1
	    denom = (denom + 2)
	    pwr = pwr + 1
	     
    return pi_approx

digits = int(input("How many digits of pi would you like to approximate? "))
pi_initial_total = my_pi(digits)
pi_total = (12 ** (1/2)) * pi_initial_total

print("The approximation of pi to", digits, "digits is:", pi_total)