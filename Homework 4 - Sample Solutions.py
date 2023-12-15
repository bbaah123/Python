# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 05:52:33 2023

@author: USER
"""

cities = ['New York', 'Columbus', 'Chicago', 'San Francisco', 'Los Angeles', 'Houston']

numbers = [55, 65, 75, 85, 95]

states = ['New York', 'Ohio', 'Illinois', 'California', 'California', 'Texas']

fruits = ['Apple', 'Banana', 'Cherry', 'Mango', 'Strawberry']

adjectives = ['big', 'green', 'small', 'juicy', 'red']

# 1. Create a list called 'sports' and print it.
sports = ['Soccer', 'Basketball', 'Tennis', 'Golf', 'Cricket']
print(sports)

# 2. Print each number in 'numbers' followed by its square.
for number in numbers:
    print(number, number ** 2)

# 3. Create 'vegetables' list, combine it with 'fruits', and print the combined list.
vegetables = ['Carrot', 'Broccoli', 'Spinach', 'Cucumber']
combined_list = fruits + vegetables
print(combined_list)

# 4. Create 'descriptions' by combining 'adjectives' and 'fruits' elements and print it.
descriptions = [adj + ' ' + fruit for adj, fruit in zip(adjectives, fruits)]
print(descriptions)

# 5. Remove the last element from 'cities' and print the updated list.
cities.pop()
print(cities)

# 6. Check if 'Grapes' is in 'fruits' and print 'Yes' or 'No'.
if 'Grapes' in fruits:
    print("Yes")
else:
    print("No")

# 7. Replace the third element of 'states' with 'Florida' and print the updated list.
states[2] = 'Florida'
print(states)

# 8. Slice 'numbers' to create 'subset' and print it.
subset = numbers[1:4]
print(subset)

# 9. Create a sorted copy of 'cities' as 'cities_copy' and print both lists.
cities_copy = cities.copy()
cities_copy.sort()
print("Original cities list:", cities)
print("Sorted cities_copy list:", cities_copy)

# 10. Count the occurrences of 'California' in 'states' and print the count.
count_california = states.count('California')
print("Count of 'California':", count_california)

# 11. Insert 'Pineapple' at index 2 in 'fruits' and print the updated list.
fruits.insert(2, 'Pineapple')
print(fruits)

# 12. Remove the element at index 4 from 'adjectives' and print the updated list.
del adjectives[4]
print(adjectives)

# 13. Create 'mixed' by combining 'fruits' and 'numbers' and print it.
mixed = fruits + numbers
print(mixed)

# 14. Reverse the order of elements in 'states' and print the reversed list.
states.reverse()
print(states)

# 15. Check if 'numbers' is empty and print 'Empty' or 'Not empty'.
if not numbers:
    print("Empty")
else:
    print("Not empty")

# 16. Find and print the maximum number in 'numbers'.
max_number = max(numbers)
print("Maximum number:", max_number)

# 17. Find the index of 'Chicago' in 'cities' and print it.
index_chicago = cities.index('Chicago')
print("Index of 'Chicago':", index_chicago)

# 18. Remove all occurrences of 'Apple' from 'fruits' and print the updated list.
fruits = [fruit for fruit in fruits if fruit != 'Apple']
print(fruits)

# 19. Add 'Lemon' and 'Orange' to 'fruits' and print the updated list.
fruits.extend(['Lemon', 'Orange'])
print(fruits)

# 20. Create 'even_numbers' with even numbers from 'numbers' and print it.
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
