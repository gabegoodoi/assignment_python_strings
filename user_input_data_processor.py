'''
Objective: The aim of this assignment is to process and format user input data.

Task 1: Input Length Validator 
Write a script that asks for and checks the length of the user's first name and last name. 
Both should be at least 2 characters long. If not, print an error message.
'''

while True:
    first_name = input("What's your first name? ")
    if len(first_name) < 2:
        print("ERROR: your first name is too short.")
    else:
        break
while len(first_name) >= 2:
    last_name = input("What's your last name? ")
    if len(last_name) < 2:
        print("ERROR: your last name is too short.")
    else:
        print(f"Nice name, {first_name} {last_name}. Goodbye!")
        break