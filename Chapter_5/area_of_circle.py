#A program that returns the area of a circle given a radius
import math

print("This program finds the area of a circle given its radius.")

def areaOfCircle(r):
    Area = math.pi*r**2
    return Area

radius = int(input("Please enter the radius of the circle you wish to find the area of: "))
TotalArea = areaOfCircle(radius)

print("The area of a circle with the radius of", radius, "is", TotalArea)