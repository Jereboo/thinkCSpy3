"""Using the text file studentdata.txt (shown in exercise 1) write a program that 
calculates the average grade for each student, and print out the student’s name along 
with their average grade.""" 

fileref = open("studentdata.txt", "r")

for line in fileref:
	grades = line.split()
	name = grades[0]
	actual_grades = grades[1:]
	for position in range(len(actual_grades)):
		actual_grades[position]= int(actual_grades[position])
	average = sum(actual_grades) / len(actual_grades)
	print(name, "has an average grade of", average)

fileref.close()