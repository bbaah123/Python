# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 06:15:51 2023

@author: USER
"""

# Problem 1: Divisible by 3
for i in range(1, 50, 3):
    if i % 3 == 0:
        print(i, "is divisible by 3")

# Problem 2: Extract Vowels
phrase = 'Artificial Intelligence is fascinating!'
for char in phrase:
    if char.lower() in 'aeiou':
        print(char, end='')

# Problem 3: Counting by 2s
counter = 0
while counter <= 20:
    print(counter, end=' ')
    counter += 2

# Problem 4: Skipping 7
x = 0
while x <= 10:
    if x == 7:
        x += 1
        continue
    else:
        print(x, end=' ')
    x += 1

# Problem 5: Breaking the Loop (Part 2)
y = 10
while y >= 0:
    if y == 5:
        break
    print(y, end=' ')
    y -= 1
print('\nDone with the while loop')

# Problem 6: Number Guessing (Part 2)
while True:
    print("Choose a number between 1 and 10: ")
    num = int(input('1/2/3/4/5/6/7/8/9/10? '))
    if num < 1 or num > 10:
        print('You entered an invalid choice')
    else:
        print("You chose", num)
    play_again = input('Do you want to play again (y/n)? ')
    if play_again.lower() == 'n':
        break
print('Thank you for playing. Goodbye!')

# Problem 7: Play Again (Part 2)
play_again = 'y'
while play_again.lower() == 'y':
    print("Choose a number between 1 and 10: ")
    num = int(input('1/2/3/4/5/6/7/8/9/10? '))
    if num < 1 or num > 10:
        print('You entered an invalid choice')
    else:
        print("You chose", num)
    play_again = input('Do you want to play again (y/n)? ')
print('Thank you for playing. Goodbye!')

# Problem 8: Countdown (Part 2)
z = 5
while z >= -5:
    print(z, end=' ')
    z -= 1

# Problem 9: Nested Loop (Part 2)
m = 1
while m <= 3:
    n = 5
    while n <= 7:
        print(f'{m}, {n} ')
        n += 1
    m += 1

# Problem 10: Nested Loop with For (Part 2)
for m in range(1, 4):
    for n in range(5, 8):
        print(f'{m}, {n} ')

# Problem 11: List Iteration (Part 2)
cities = ['New York', 'Tokyo', 'London', 'Paris']
temperatures = [22, 28, 15, 20]
for city in cities:
    print(city)
print()
for temp in temperatures:
    print(temp)

# Problem 12: List Manipulation (Part 2)
cities.pop()
cities.reverse()
print(cities)
