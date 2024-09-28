# Exercise

# Prompt the user to enter their age as an integer.
# Based on the input, categorize the person into one of the following life stages:
# INFANT: 0 – 1 YEAR
# Toddler: 2 – 3 years
# Child: 4 – 12 years
#Teenager: 13 – 19 years
# Adult: 20 – 64 years
# Senior: 65 years and older
# Display the appropriate life stage
# If the user enters a negative number or a non-realistic number (eg: more than 150) display an ‘invalid age’ message.
# Display on the screen: Provide the screenshot and github link
# Submit your homework in your github account as well. Create a folder Python-codes 

# Operation
# Main program to prompt user for their age

try: 
    user_age = int(input("Please enter your age as an integer: \t"))
    
    # Categorize based on the input
    if user_age < 0 or user_age > 150:
        life_stage = "Invalid age! Please enter a realistic age between 0 and 150."
    elif user_age <= 1:
        life_stage = "INFANT"
    elif 2 <= user_age <= 3:
        life_stage = "Toddler"
    elif 4 <= user_age <= 12:
        life_stage = "Child"
    elif 13 <= user_age <= 19:
        life_stage = "Teenager"
    elif 20 <= user_age <= 64:
        life_stage = "Adult"
    else:
        life_stage = "Senior"
    
    # Print the life stage
    print(f"Based on your age, you are categorized as: {life_stage}")
    
except ValueError:
    print("Invalid input! Please enter a valid integer for your age.")
