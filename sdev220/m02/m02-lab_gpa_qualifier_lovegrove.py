"""
Author: Terry Lovegrove
File: m02-lab_gpa_qualifier_lovegrove.py
Date: 2025-01-24
Assignment: Module 2 Lab - Case Study: if...else and while
Purpose: Get student GPA info to test for Honor Roll vs Dean's list qualifiers

"""
# Set Defaults

DEANS_LIST = 3.5
HONOR_ROLL = 3.25
gpa = 0
first_name = ''
last_name = input("Enter your last name, or enter 'ZZZ' to quit.\n")

while last_name != "ZZZ":
    print(f"You entered {last_name}.")
    first_name = input("Thanks! Now please enter your first name to continue.\n")
    print(f"Hello {first_name} {last_name}.")
    gpa = float(input("Please enter your GPA.\n"))
    print(f"Your gpa is {gpa}.")
    if gpa >= DEANS_LIST:
        print("You made the Dean's list!\n")
    elif gpa >= HONOR_ROLL:
        print("You made the Honor roll!\n")
    else:
        print("You did not make the Dean's List or the Honor roll.\n")
    last_name = input("Enter your last name, or enter 'ZZZ' to quit.\n")