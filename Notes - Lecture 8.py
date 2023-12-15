# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 07:29:18 2023

@author: USER
"""

countries = ['Nigeria', 'South Africa', 'Kenya', 'Zimbabwe', 'USA', 'Canada', 'France']
countries_with_e = []
for country in countries:
    if 'e' in country:
        countries_with_e.append(country)
print(countries_with_e)
    

new_countries_list = [country for country in countries if 'e' in country]
print(new_countries_list)

#Remove the first occurance of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i] , end=' ')
  i = i + 1
print()  
for fruit in thislist:
    print(fruit, end=' ')
print()  
for i in range(len(thislist)):
    print(thislist[i], end=' ')
print()

#list comprehension  
thislist = ["apple", "banana", "cherry"]
[print(x, end=' ') for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if x != "apple"]
           
#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)

#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


#Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

person ={
    'name':'Bill',
    'age': '65',
    'city': 'Seattle'
    }

print(person)

print('\nHere are Bills details')
for key, value in person.items():
    print(key, value)


print('\nHere are keys')
for key in person.keys():
    print(key)
    

print('\nHere are values')
for value in person.values():
    print(value)
    
print()   
print(person['name'])
print(person['age'])
print(person['city'])

print()
print(person.get('name'))

person['name'] = 'Jeff'
print(person['name'])

person['age'] = 55
print(person['age'])

del person['city']
print(person)

person['state']='Washington'
print(person)

# Nested Dictionaries
employee = {
    'name': 'Bob',
    'department': {
        'name': 'Engineering',
        'position': 'Software Developer'
    }
}

print(employee['department']['position'])  # Output: 'Software Developer'