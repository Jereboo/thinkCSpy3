"""Task: Write a function is_rightangled which, given the length of three sides of a triangle, 
    will determine whether the triangle is right-angled. Assume that the third argument to
    the function is always the longest side. It will return True if the triangle is 
    right-angled, or False otherwise.

    Hint: floating point arithmetic is not always exactly accurate, so it is not safe to 
    test floating point numbers for equality. If a good programmer wants to know whether 
    x is equal or close enough to y, they would probably code it up as:

if  abs(x - y) < 0.001:      # if x is approximately equal to y
    ...

-----------------------    
Their clever ass code:

from test import testEqual

def is_rightangled(a, b, c):
    is_rightangled = False

	#mine- This series of conditionals structures itself by the three possible equations \ 
	    that could result after finding the longest side(hypot) by comparing a & b & c
    if a > b and a > c: 
        is_rightangled = abs(b**2 + c**2 - a**2) < 0.001
    elif b > a and b > c:
        is_rightangled = abs(a**2 + c**2 - b**2) < 0.001
    else:
        is_rightangled = abs(a**2 + b**2 - c**2) < 0.001
    return is_rightangled

testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(4.0, 8.0, 16.0), False)
testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.4, 0.64031), True)
-------------------------"""
    
#A program that tells if a triangle is right angled given the length of its sides

def is_right_angled(a, b, c):
    sides_lst = [a, b, c]
    sorted_sides = sorted(sides_lst)
    side_a = sorted_sides[0]
    side_b = sorted_sides[1]
    side_c = sorted_sides[2]
    sides = side_a ** 2 + side_b ** 2
    hypot = side_c ** 2
    
    """The following is my work trying to make this same function without using lists. 
        It failed. :(
    
    #side_c = max(a, b, c) #finds which side is the hypot, by finding the longest side
    #print(side_c)
    #other_sides = a + b + c - side_c #finds sides a & b by finding opposites of the longest side
    #print(other_sides)
    #for i in range(2): #runtime error- I still have not isolated a or b
        #sides = sides + other_sides ** 2 #runtime error this line == a+b**2 iterated twice
    #print(sides)
    #hypot = side_c ** 2"""
    
    if abs(sides - hypot) < 0.001:
        return True
    else:
        return False


side_1 = float(input("Enter side 1: "))
side_2 = float(input("Enter side 2: "))
side_3 = float(input("Enter side 3: "))

print(is_right_angled(side_1, side_2, side_3))
