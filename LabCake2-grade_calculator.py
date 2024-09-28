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
        return 'E'

# Gather grades using list comprehension
grades = [float(input(f"Enter your grade for subject {x+1}: ")) for x in range(5)]

# Calculate the average grade
average_grade = sum(grades) / len(grades)

# Get the letter grade
letter_grade = determine_letter_grade(average_grade)

# Printing the average grade and the corresponding letter grade
print(f"Your average grade is: {average_grade:.2f}")
print(f"Your letter grade is: {letter_grade}")
