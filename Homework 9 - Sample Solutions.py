# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 05:10:27 2024

@author: USER
"""

import datetime

# Problem 1: File Content Analysis
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        return "File not found."

print(count_lines('data.txt'))

# Problem 2: Updating File Content
def append_datetime(filename):
    with open(filename, 'a') as file:
        file.write(str(datetime.datetime.now()) + '\n')

append_datetime('log.txt')

# Problem 3: Reading Specific Lines
def read_specific_lines(filename, line_numbers):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return [lines[i] for i in line_numbers if i < len(lines)]
    except FileNotFoundError:
        return "File not found."

print(read_specific_lines('example.txt', [0, 2, 4]))

# Problem 4: Search for a Word
def search_word(filename, word):
    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                if word in line:
                    print(f'Line {i}: {line.strip()}')
    except FileNotFoundError:
        print("File not found.")

search_word('example.txt', 'Python')

# Problem 5: File Conversion
def convert_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line.upper())

convert_file('input.txt', 'output.txt')

# Problem 6: Division Calculator with Error Handling
def division_calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 / num2)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid input. Please enter a number.")

#Sample Solution: Custom Exception for User Age
class AgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message):
        self.message = message

def ask_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise AgeError("Age cannot be negative.")
        return age
    except AgeError as error:
        print(f"Error: {error.message}")

#Sample Solution: File Processing with Exception Handling
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Sample Solution: Assertive Input Validation
def validate_positive_number():
    try:
        number = int(input("Enter a number: "))
        assert number > 0, "Number must be positive"
        print("Valid number entered.")
    except AssertionError as error:
        print(f"AssertionError: {error}")

#Sample Solution: Handling Multiple Exceptions
def read_user_file():
    try:
        filename = input("Enter a file name: ")
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except IsADirectoryError:
        print("The specified path is a directory, not a file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage of each function
ask_age()
read_file('example.txt')
validate_positive_number()
read_user_file()
