#A program that will convert degrees F into C

f = float(input("What is the temperature in degrees fahrenheit? "))
celsius = (f - 32) * (5/9)

print (f, "degrees fahrenheit is", celsius, "degrees celsius")