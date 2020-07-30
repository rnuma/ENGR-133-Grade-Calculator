#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     e.g. Python Final Project (Main Program) 
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

import PythonFinalProject_Script

# Imports the user defined functions in the script file that are used to calculate
    # final course grade, letter grade, and whether student passed of failed the class

def Section_Grades():
    
# User defined function that takes the user-inputed the number values for each 
    # ENGR 133 section into the user defined functions in the script file for calculation
    
    matrixStudents = []
    
# Creates a matrix containing the grading information for each student
    
    numStudents = int(input("How many students are in the class: "))
    
# Asks the user to input number of students in the class
    
    for i in range(numStudents):
        grade_info = []
        name = input("Enter Student's name: ")
        grade_info.append(name)
        
# for loop iterates (runs) however many times based of the number of students in the class
    # for loop iterates through student's name, calculated total
        
        Participation = int(input("Enter final participation grade here: "))
        if Participation < 0 or Participation > 100:
            print("Total participation grade must be between 0 and 100.")
            return 
        Quizzes = int(input("Enter final quiz grade here: "))
        if Quizzes < 0 or Quizzes > 100:
            print("Total quiz grade must be between 0 and 100.")
            return
        PostACT = int(input("Enter final post activity grade here: "))
        if PostACT < 0 or PostACT > 100:
            print("Total post activity grade must be between 0 and 100.")
            return
        EYM = int(input("Enter final engineering your major exploration grade here: "))
        if EYM < 0 or EYM > 100:
            print("Total engineering your major exploration grade must be between 0 and 100.")
            return
        PythonProject = int(input("Enter final python project grade here: "))
        if PythonProject < 0 or PythonProject > 100:
            print("Total python project grade must be between 0 and 100.")
            return 
        MatlabProject = int(input("Enter final matlab project grade here: "))
        if MatlabProject < 0 or MatlabProject > 100:
            print("Total matlab project grade must be between 0 and 100.")
            return
        Exams = int(input("Enter total exam(s) grade here: "))
        if Exams < 0 or Exams > 100:
            print("Total exam(s) grade must be between 0 and 100.")
            return
        
# Asks the user to input a number grade between 0 to 100 for section in ENGR 133
        
# If a number inputed is not between 0 and 100, the program will display an error message
    # and require the user to rerun the entire program 
        
        print("-----------------------------------")
        
# Print a dashed line that seperates the grading information for each student
        
        EngSections = [ Participation, Quizzes, PostACT, EYM, PythonProject, MatlabProject, Exams]
        GradeAVG = PythonFinalProject_Script.Average_Calculator(EngSections)
        grade_info.append(GradeAVG)
        matrixStudents.append(grade_info)
        
# Inputs user-inputed number grades for each ENGR 133 section into the average 
    # grade calculator (in the script file)
# Places the final calculated course grade into the matrix with grade information for the student
        
    i = 0
    while(i < numStudents):
        for j in range(2):
            if(j == 0):
                print("Student:", matrixStudents[i][j])
            elif(j == 1):
                print(round(matrixStudents[i][j],2))
                PythonFinalProject_Script.Letter_Grade(matrixStudents[i][j])
                PythonFinalProject_Script.Pass_Fail(matrixStudents[i][j])
                print("-----------------------------------")
        i = i+1
    return

# Prints the student name, final course grade, letter grade, and pass / fail statement<
    # using a for loop, into a matrix by iterating through each number of students using 
    # a while loop and printing
   
    PythonFinalProject_Script.Letter_Grade(GradeAVG)
    PythonFinalProject_Script.Pass_Fail(GradeAVG)
    
    #Traces back total course grade for each student into the user defined functions
        # in the script file to determine letter grade and pass / fail for each student
    
Section_Grades()

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''