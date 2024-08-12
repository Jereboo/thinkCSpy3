"""---------------------------------------------
Task: Implement the calculator for the date of Easter.

The following algorithm computes the date for Easter Sunday for any year between 1900 to 
2099.

Ask the user to enter a year. Compute the following:

        a = year % 19 #m- number of lunar cycles in a year?
        b = year % 4 #m- ?
        c = year % 7 #m- days in a week?
        d = (19 * a + 24) % 30 #m- somehow converting lunar cycles into days of the month?
        e = (2 * b + 4 * c + 6 * d + 5) % 7 #m-WTF?
        dateofeaster = 22 + d + e #m- What value will this be returning?- Day of the year?
        Week of the year?

Special note: The algorithm can give a date in April. Also, if the year is one of four 
special years (1954, 1981, 2049, or 2076) then subtract 7 from the date.

Your program should print an error message if the user provides a date that is out of 
range.

Their code:

year = int(input("Please enter a year"))
if year >= 1900 and year <= 2099: #m- I forgot to make an error conditional
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    dateofeaster = 22 + d + e

    if year == 1954 or year == 2981 or year == 2049 or year == 2076:
        dateofeaster = dateofeaster - 7

    if dateofeaster > 31: #I didn't understand what value was being returned until I saw these last two conditional statements
        print("April", dateofeaster - 31)
    else:
        print("March", dateofeaster)
else:
    print("ERROR...year out of range")


-------------------------------------------------"""

#A program that calculates the date of Easter for any year between 1900 to 2099.

print("This program finds the date for Easter for any year between 1900 to 2099.")

def easter_date(year):        
    if year >= 1900 and year <= 2099:
    	a = year % 19
    	b = year % 4
    	c = year % 7
    	d = (19*a + 24) % 30
    	e = (2*b + 4*c + 6*d + 5) % 7
    	dateofeaster = 22 + d + e

    	if year == 1954 or year == 2981 or year == 2049 or year == 2076:
        	dateofeaster = dateofeaster - 7

    	if dateofeaster > 31:
        	print("April", dateofeaster - 31)
    	else:
        	print("March", dateofeaster)
        	
    else:
    	print("ERROR...year out of range")
    
    """My original code:
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    date_of_easter = 22 + d + e
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        date_of_easter = date_of_easter - 7
        print(date_of_easter)        
    else:
        print(date_of_easter)"""


year_in_question = int(input("Please enter a year to find the date for Easter in that " \
    "year: "))

easter_date(year_in_question)
