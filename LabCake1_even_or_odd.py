#Exercice:

# Write a program that will ask user for a number than check
# whether that number is EVEN or ODD. >
# Display on the screen:
# Please enter a number between 1-100.
# Your number user_number is even/odd.

#Operation
# asking the user to privide a number
user_number = int(input("enter you choosen your number between 1 - 100:\t"))
# Checking if the user-number is even or odd
if user_number % 2 == 0:
        print(f"Your number {user_number} is even.")
elif user_number % 2 == 1:
        print(f"Your number {user_number} is odd.")
else:
        print("Invalid input! Please enter a number between 1 and 100") 