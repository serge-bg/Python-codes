# EXERCISE: 
# Write a Python program that prints the largest and smallest values in a list.
# Print the two values on the same line, separated by a space.
# The largest value should appear first and the smallest value should appear second.
# You may assume that the list only contains numeric values
# If the list is empty, print "None."

# Expected                 output:
# [3,4,5,6]       -->      6 3
# [-1,-2,-3,-4]     -->     -1 -4
# [0,0,0,0]          -->     0 0
# []                  -->     []

# OPERATION

# List of number list
number_list = [
    [3, 4, 5, 6],       # Expected Output: 6 3
    [-1, -2, -3, -4],   # Expected Output: -1 -4
    [0, 0, 0, 0],       # Expected Output: 0 0
    []                  # Expected Output: None
]

# Loop through each number list
for my_list in number_list:
    if len(my_list) == 0:
        print("None")
    else:
        print(max(my_list), min(my_list))


