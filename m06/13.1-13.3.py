"""
Author: Terry Lovegrove
File: m06.py
Date: 2025-02-19
Assignment: Module 6 Programming Assignment -Concurrency in Python
13.1 Write the current date as a string to the text file today.txt.
13.2 Read the text file today.txt into the string today_string.
13.3 Parse the date from today_string.
15.1 Use multiprocessing to create three separate processes. 
Make each one wait a random number of seconds between zero and one, 
print the current time, and then exit.
"""


from datetime import datetime

the_file = 'today.txt'
current_time = datetime.now()


# 13.1 Write the current date as a string to the text file today.txt.

with open(the_file, 'w') as file:
    file.write(str(current_time))

print(f'we wrote {current_time} to {the_file}.')


# 13.2 Read the text file today.txt into the string today_string.

print('We will now read the file and grab that data.')

with open(the_file,'r') as file:
    today_string = file.readline()

print(f'Data read from the file: {today_string}')


# 13.3 Parse the date from today_string.

format_data = "%Y-%m-%d %H:%M:%S.%f"

parsed_date = datetime.strptime(today_string, format_data)

print(f"Formatting used to break down the date: {format_data}")
print(f'Parsed date below using the formatting.')

print(f'Current year: {parsed_date.year}')
print(f'Current month: {parsed_date.month}')
print(f'Current day: {parsed_date.day}')
print(f'Current hour: {parsed_date.hour}')
print(f'Current minute: {parsed_date.minute}')
print(f'Current second: {parsed_date.second}')
print(f'Current microsecond: {parsed_date.microsecond}')


