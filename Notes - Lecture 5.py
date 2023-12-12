# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:52:31 2023

@author: USER
"""

greeting ="Welcome to the Data Analysis, Machine Learning and AI Program"

print(greeting.upper())

print(greeting.lower())

print(greeting.title())

print(greeting.capitalize())

status = "   True    "
txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)
print(status)
print(status.strip())


path ="C:\\users\\user\\desktop\\bootcamp\n"
print(path)

txt = "We are the \t\t\t so-called \"Vikings\" from the north."
print(txt) 


txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)


txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)


#Check if all the characters in the text are alphanumeric:

txt = "Company12"

x = txt.isalnum()

print(x)


#Check if all the characters in the text are letters:
txt = "CompanyX"

x = txt.isalpha()

print(x)


#Check if all the characters in the text are digits:
txt = "50800"

x = txt.isdigit()

print(x)


#Check if all the characters in the text are in lower case:
txt = "hello world!"

x = txt.islower()

print(x)


#Check if all the characters in the text are in upper case:
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

"""
A string must be specified as the separator.
string.join(iterable)
"""
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)


#Join all items in a tuple into a string, using a hash character as separator
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
