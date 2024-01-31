# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:08:51 2023

@author: USER
"""

# 1. Function Basics
def calculate_area(length, width):
    return length * width

# Test the function
print(calculate_area(5, 3))

# 2. Default Arguments
def calculate_area(length=1, width=1):
    return length * width

# Test the function
print(calculate_area())
print(calculate_area(5))
print(calculate_area(5, 3))

# 3. Variable-length Arguments (*args)
def concatenate_strings(*args):
    return ' '.join(args)

# Test the function
print(concatenate_strings("Hello", "world!"))
print(concatenate_strings("I", "love", "Python"))

# 4. Keyword Arguments (**kwargs)
def build_vehicle(**kwargs):
    return kwargs

# Test the function
print(build_vehicle(make="Toyota", model="Corolla", year=2020, color="Blue"))

# 5. Class Creation
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_description(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"

# Test the class
book = Book("1984", "George Orwell", 1949)
print(book.get_description())

# 6. Inheritance
class EBook(Book):
    def __init__(self, title, author, publication_year, file_size):
        super().__init__(title, author, publication_year)
        self.file_size = file_size

    def is_large(self):
        return self.file_size > 100

# Test the subclass
ebook = EBook("1984", "George Orwell", 1949, 105)
print(ebook.is_large())  # Output: True

# 7. Using super()
class EBook(Book):
    def __init__(self, title, author, publication_year, file_size):
        super().__init__(title, author, publication_year)
        self.file_size = file_size

    def get_description(self):
        return super().get_description() + f", File Size: {self.file_size}MB"

# Test the method
ebook = EBook("1984", "George Orwell", 1949, 105)
print(ebook.get_description())

# 8. Combining Function Arguments
def create_user_profile(username, email, *interests, **user_details):
    profile = {
        'username': username,
        'email': email,
        'interests': interests,
        'details': user_details
    }
    return profile

# Test the function
print(create_user_profile('johndoe', 'john@example.com', 'coding', 'reading', age=30, country='USA'))

# 9. Error Handling in Functions
def calculate_area(length, width):
    try:
        return length * width
    except TypeError:
        print("Error: Both length and width must be numbers.")

# Test the function
print(calculate_area(5, 'three'))

# 10. Practical Application
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Test the methods
print(TemperatureConverter.celsius_to_fahrenheit(0))  # Output: 32.0
print(TemperatureConverter.fahrenheit_to_celsius(32))  # Output: 0.0
