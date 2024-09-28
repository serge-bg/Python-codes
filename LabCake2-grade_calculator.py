#Exercise
# Write a program that will ask a student for their grades in 5 subjects.
# Calculate your average grade and print grade from A-E.
# A>90
# B>80
# C>70
# D>60
# E===Failed
# Display on the screen:  Provide the screenshot and github link.  Submit your homework in your github account as well.  Create a folder in Python-codes

# Operation
# Input grades for five subjects
subject1_grade = float(input("Please enter subject1 grade: \t"))
subject2_grade = float(input("Please enter subject2 grade: \t"))
subject3_grade = float(input("Please enter subject3 grade: \t"))
subject4_grade = float(input("Please enter subject4 grade: \t"))
subject5_grade = float(input("Please enter subject5 grade: \t"))

# Determining letter grade based on the average grade
def determine_letter_grade(avg_grade):
    if avg_grade > 90:
        return 'A'
    elif avg_grade > 80:
        return 'B'
    elif avg_grade > 70:
        return 'C'
    elif avg_grade > 60:
        return 'D'
    else:
        return 'E===Failed'

# Calculate the average grade
average_grade = (subject1_grade + subject2_grade + subject3_grade + subject4_grade + subject5_grade) / 5

# Get the letter grade based on the average
letter_grade = determine_letter_grade(average_grade)

# Display the average grade and corresponding letter grade
print(f"Your average grade is: {average_grade:.2f}")
print(f"Your letter grade is: {letter_grade}")


