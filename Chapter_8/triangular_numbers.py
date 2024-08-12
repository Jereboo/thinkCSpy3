"""A program that prints out the number of dots composing increasingly large equilateral 
    triangles (Triangular Numbers)"""
    
def print_triangular_numbers(number):
    n = 0
    for i in range(number):
        n = n + (i + 1)
        print(i, "\t", n)
        
    """while n != number: #How can I achieve the same thing with a while loop? Is it easier to use a for loop?
        current_n = n
        n = n + (n + 1)
        print(current n, "\t", n)"""
    

to_test = int(input("What number do you want the pattern to go to? "))

print_triangular_numbers(to_test)