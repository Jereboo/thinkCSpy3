"""-----
Print out a neatly formatted multiplication table, up to 12 x 12.
-----"""

"""I struggled with this one pretty bad!"""

#A program that creates a multiplication table

#creates each column
def column_multiples(every_row, highest_number):
	for every_column in range(1, highest_number + 1):
		print(every_row * every_column, end = "\t")
	print()


#creates each row by calling the column function to establish the first row and build each row incrementally from there
def multiples_table(highest_number):
	for every_row in range(1, highest_number + 1):
		column_multiples(every_row, highest_number)

to_table = int(input("Please enter how high you would like your multiplication table to be: "))

multiples_table(to_table)
