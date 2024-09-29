#Exercice:

# Write a program that will ask user for a number than check
# whether that number is EVEN or ODD. >
# Display on the screen:
# Please enter a number between 1-100.
# Your number user_number is even/odd.

#Operation
# Asking the user to provide a number
# Asking the user to provide a number
user_number = int(input("Enter your chosen number between 1 - 100:\t"))

# Checking if the user-number is within the valid range
if user_number < 1 or user_number > 100:
    print("Invalid input! Please enter a number between 1 and 100.")

elif user_number % 2 == 0:
        print(f"Your number {user_number} is EVEN.")
else:
    if user_number % 2 != 0:
        print(f"Your number {user_number} is ODD.")

