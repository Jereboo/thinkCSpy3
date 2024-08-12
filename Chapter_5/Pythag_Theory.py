#A program that finds the hypotenuse of a right triangle w/ the length of two sides
import math

print("This program will find the length of a hypotenuse in a right triangle if you input the other two sides.")
x = int(input("What is the length of the first side? "))
y = int(input("What is the length of the second side? "))
hypot = math.hypot(x, y)

print("The length of the hypotenuse is:", hypot)