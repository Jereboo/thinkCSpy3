"""Using the text file studentdata.txt (shown in exercise 1) write a program that
calculates the minimum and maximum score for each student. Print out their name as well."""

fileref = open("studentdata.txt", "r")

for line in fileref:
	orig_line = line.split()
	name = orig_line[0]
	grades = orig_line[1:]
	for position in range(len(grades)):
		grades[position] = int(grades[position])
	grades.sort()
	#for position in range(len(grades)):
		#if grades[position] > grades[position - 1]:
			#grades[position + 1] = grades[position]
	print("The lowest grade", name, "has is:", grades[0], "and the highest grade", name, "has is:", grades[-1])

fileref.close()