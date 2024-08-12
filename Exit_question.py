#A program that exits python3 interactive <-- does not currently work in interactive python (this defeats the purpose...)

import string

def ext_py_int(exit_decision):
    while exit_decision != "YES":
    	if exit_decision != "NO":
    	    exit_decision_initial = input('Error: Please input either "Yes" or "No" ')
    	    exit_decision = exit_decision_initial.upper()
    	elif exit_decision == "NO":
    	    break 
    exit()
    	    

exit_question = input('Would you like to exit interactive Python? (Enter "Yes" to exit or "No" to continue) ')
exit_question_upper = exit_question.upper()

ext_py_int(exit_question_upper)