def get_grade(grade):
    if grade >= 90:
        mark = "A"
        return mark
        
    elif grade >= 80: #and grade < 90:
        mark = "B"
        return mark
    
    elif grade >= 70: #and grade < 80:
        mark = "C"
        return mark
    
    elif grade >= 60: #and grade < 70:
        mark = "D"
        return mark
    
    else:
        mark = "F"
        return mark
        
to_grade = float(input("Input grade: "))
grade_mark = get_grade(to_grade)

print("Your grade is a", grade_mark)