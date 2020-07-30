#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     e.g. Python Final Project (Script)
	Author:         Roan Numa, rnuma@purdue.edu
	Team ID:        003-19 (e.g. 001-14 for section 1 team 14)
	
Contributor:    Name, login@purdue [repeat for each]
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
def Average_Calculator(m):
    GradeAVG = ((m[0] * 0.05) + (m[1] * 0.05) + (m[2] * 0.10)
                + (m[3] * 0.10) + (m[4] * 0.15) + (m[5] * 0.15) + (m[6] * 0.40))
    return GradeAVG

# User defined funciton that multiplies the accurate weight for each ENGR 133 section
    # by the grades inupted by the user, then adds each individual section grade to produce 
    # the final course grade
   
def Letter_Grade(grade):
    if grade >= 94:
        print("A")
    elif grade >= 90 and grade < 94:
        print("A-")
    elif grade >= 87 and grade < 90:
        print("B+")
    elif grade >= 84 and grade < 87:
        print("B")
    elif grade >= 80 and grade < 84:
        print("B-")
    elif grade >= 77 and grade < 80:
        print("C+")
    elif grade >= 74 and grade < 77:
        print("C")
    elif grade >= 70 and grade < 74:
        print("C-")
    elif grade >= 60 and grade < 70:
        print("D")
    elif grade < 60:
        print("F")
    else:
        return "F"
    
# User defined function that uses if-elif-else statements that helps determine
    # the letter grade for the student based of their total course grade

def Pass_Fail(grade):
    if grade >= 94:
        print("Pass")
    elif grade >= 90 and grade < 94:
        print("Pass")
    elif grade >= 87 and grade < 90:
        print("Pass")
    elif grade >= 84 and grade < 87:
        print("Pass")
    elif grade >= 80 and grade < 84:
        print("Pass")
    elif grade >= 77 and grade < 80:
        print("Pass")
    elif grade >= 74 and grade < 77:
        print("Pass")
    elif grade >= 70 and grade < 74:
        print("Pass")
    elif grade >= 60 and grade < 70:
        print("Fail")
    elif grade < 60:
        print("Fail")
    else:
        return "Fail"

# User defined funcion that uses if-elif-else statements that helps determine whether
    # the student passed or failed the course based off their final course grade

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''