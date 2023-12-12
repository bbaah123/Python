# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 08:09:12 2023

@author: Bernard Baah
@email: contact@fillycoder.com
@website: https://fillycodergh.com
"""


greeting = "Welcome to the Data Analysis, Machine Learning, and AI Bootcamp"
print(greeting)

print(greeting[2:10])

print(greeting[:10])

print(greeting[5:])


first_name = "Lemuel"
last_name = "Baah"

full_name = first_name + " " + last_name
print(full_name)

age = 18

print("Your age is " + str(18))

date_of_birth = input("Enter your date of birth: ")
print(date_of_birth)


age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")

print("Your age is " + str(age))
    
print("Your age is",  age)

print ("Your age is {}".format(age))

print(f"Your age is {age}")

name = input("Enter your name: ")
print("Your name is", end=" ")
print(name)


for x in range(10):
    print(x, end=" ")

print()    
b = "Hello, World!"
print(b[-5:-2])

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello# World!"
print(a.split("#")) # returns ['Hello', ' World!']

a="  Testing mic 123  "
print(a)
print(a.strip())
age = input("Enter your age: ")
print(f"Your age is {age}")

if int(age)>=18:
    print("You are eligible to vote")
    
status = input("Python programming is fun (T/F?)")

if(status.strip() == "T"):
    print("You rock!")
else:
    print("You suck!")
    
#Use the format() method to insert numbers into strings:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print("I want {} pieces of item {} for {} dollars.".format(quantity, itemno, price))



#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print( "I want to pay {2} dollars for {0} pieces of item {1}.".format(quantity, itemno, price))
