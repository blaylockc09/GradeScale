# Convert a numerical grade entered to a letter grade.
# Chris Blaylock
# 09/18/2019

#Named constants
# You can use the magic numbers below (89.5, 79.5, etc. as named constants, just
# figure this out and how to properly name them. 
INVALID = 101 
GRADE_A = 89.5
GRADE_B = 79.5
GRADE_C = 69.5
GRADE_D = 59.5
GRADE_F = 0
# Prompt the user to enter a numerical grade
numberGrade = float(input("Enter a numerical grade: "))

# Determine the letter grade based on the numerical grade entered.
if numberGrade >= INVALID:
    print ("Invalid Score")
elif numberGrade >= GRADE_A:
    print ("The letter grade is an A")
elif numberGrade >= GRADE_B:
    print ("The letter grade is an B")
elif numberGrade >= GRADE_C:
    print ("The letter grade is an C")
elif numberGrade >= GRADE_D:
    print ("The letter grade is an D")
elif numberGrade >= GRADE_F:
    print ("The letter grade is an F")
else:
    print("Invalid Score")
    
# If the number is higher less than 0 or more than 100, display "invalid score".

