# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:00:06 2023

@author: USER
"""

cities = ['New York', 'Columbus', 'Chicago', 'San Francisco', 'Los Angeles', 'Houston']

numbers = [55, 65, 75, 85, 95]

states = ['New York', 'Ohio', 'Illinois', 'California', 'California', 'Texas']

fruits = ['Apple', 'Banana', 'Cherry', 'Mango', 'Strawberry']

adjectives = ['big', 'green', 'small', 'juicy', 'red']

print(fruits)

for fruit in fruits:
    print(fruit, end=' ')
print()   
for i in range(len(fruits)):
    print (fruits[i])
print()     
for i in range(len(cities)):
    print(cities[i] + ", " + states[i])

print() 
    
for x in adjectives:
    for y in fruits:
        print(f"{x}, {y}")
    
fruits.append("Watermelon")
print() 
print(fruits)

fruits.remove('Mango')
print(fruits)

numbers.insert(2, 70)
print(numbers)

fruits.insert(0, 'Watermelon')
print(fruits)

item = fruits.pop()
print(fruits)
print(item)

del numbers[2]
print(numbers)
numbers.clear()
print(numbers)

del fruits[1]
print(fruits)

print(cities)
print(len(cities))
cities.append('Columbus')
print(cities)
print(cities.count('Columbus'))

print(len(cities))

cities.sort()
print(cities)

cities.reverse()

print(cities)

#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist[1] = 'mango'
print(thislist)

#-1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
    print('No')
    

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)