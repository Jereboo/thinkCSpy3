#A Program that prints "True" if a number is a prime number and "False" if not
"""My overthinking ensues below: 

print("This is a program that tells you if a number is a prime number.")

def is_prime(number):
    current_number = 1 #must start from 1
    prime_check = True
    while current_number < (number + 1):
        remainder = number % current_number
        if remainder == 0:
            if current_number != 1 and current_number != number:  
            #checks to see if the current number is either 1 or the original number
            	prime_check = False    
			#else:
        	    #prime_check = True
        elif remainder != 0:
            prime_check = True
            
        current_number = current_number + 1 #this should be at the end of the while loop
        
    return prime_check

to_test = int(input("Please input what number you want to check: "))
result = is_prime(to_test)

print(result)"""

#Their brilliant code:

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
to_test = int(input("Please input what number you want to check: "))
result = is_prime(to_test)

print(result)