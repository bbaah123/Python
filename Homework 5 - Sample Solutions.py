# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:46:07 2023

@author: USER
"""

# 1. Lists and List Comprehension
# a. Creating 'numbers' list
numbers = list(range(1, 11))

# b. Creating 'squared_numbers' using list comprehension
squared_numbers = [x ** 2 for x in numbers]

# c. Creating 'even_numbers' using list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]

# d. Creating 'words' list
words = ["apple", "banana", "cherry", "date", "kiwi"]

# e. Creating 'word_lengths' using list comprehension
word_lengths = [len(word) for word in words]

# 2. List Manipulation
# a. Removing "date" from 'fruits'
fruits = ["apple", "banana", "cherry", "date", "kiwi"]
fruits.remove("date")

# b. Adding "grape" to the end of 'fruits'
fruits.append("grape")

# c. Sorting 'fruits' in alphabetical order
fruits.sort()

# d. Reversing the order of 'fruits'
fruits.reverse()

# 3. Dictionaries
# a. Creating 'student' dictionary
student = {
    'name': 'Alice',
    'age': 20,
    'major': 'Computer Science'
}

# b. Adding 'university' -> 'XYZ University' to 'student'
student['university'] = 'XYZ University'

# c. Checking and adding 'grade' -> 'A' if it does not exist
if 'grade' not in student:
    student['grade'] = 'A'

# d. Printing all keys and values in 'student'
for key, value in student.items():
    print(key, value)

# 4. String Manipulation
# a. Creating 'sentence' string
sentence = "Python programming is fun."

# b. Extracting and printing "programming"
programming_word = sentence[7:18]
print(programming_word)

# c. Replacing "Python" with "Java" in 'sentence'
sentence = sentence.replace("Python", "Java")

# d. Checking if 'sentence' starts with "Python"
starts_with_python = sentence.startswith("Python")

# e. Checking if 'sentence' ends with "fun."
ends_with_fun = sentence.endswith("fun.")

# 5. Conditional Statements
# a. Function to check if a number is even
def is_even(n):
    return n % 2 == 0

# b. Function to check if a letter is a vowel
def is_vowel(letter):
    return letter.lower() in ['a', 'e', 'i', 'o', 'u']

# c. Function to grade an exam score
def grade_exam(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# 6. Loops
# a. Printing prime numbers between 1 and 50
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [num for num in range(1, 51) if is_prime(num)]
print(prime_numbers)

# b. Calculating the factorial of a number
def calculate_factorial(n):
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    return factorial

# c. Printing Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

# 7. Functions
# a. Function to calculate the area of a circle
import math

def calculate_area(radius):
    return math.pi * radius**2

# b. Function to count vowels in a word
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

# c. Function to reverse a list
def reverse_list(lst):
    return lst[::-1]

# Testing the functions
print(calculate_area(5))
print(count_vowels("apple"))
print(reverse_list([1, 2, 3, 4, 5]))
