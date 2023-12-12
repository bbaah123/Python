# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:18:39 2023

@author: USER
"""

for i in range(0,100,5):
    if i%5 == 0:
       print(i, "is divisible by 5")
     
greeting = 'Python 3456 programming is fun!'

for x in greeting:
    if(x.isdigit()):
        print(x, end='')
        
print()


counter = 0

while counter <= 30:
    print(counter, end=' ')
    counter += 5


x = 0
j = 0
while  x <= 20:
    if x == 5:
        x += 1
        continue
    else:
        print(x, end=' ')
    x += 1

print()

while j < 20:
    if j==5:
        break;
    print(j, end= ' ')
    j += 1
    
print('\nDone with the while loops')



while(True):
    print("Choose a random number between 1 and 5: ")
    num = int(input('1/2/3/4/5? '))
    if(num < 1 or num > 5):
        print('You entered and invalid choice')
    else:
        print("You chose", num)
        
    play_again = input('Do you want to play again (y/n)? ')
    if play_again == 'n':
        break
    
print('Thank you for playing. Goodbye!')


play_again = 'y'

while(play_again == 'y'):
    print("Choose a random number between 1 and 5: ")
    num = int(input('1/2/3/4/5? '))
    if(num < 1 or num > 5):
        print('You entered and invalid choice')
    else:
        print("You chose", num)
        
    play_again = input('Do you want to play again (y/n)? ')
    
    
print('Thank you for playing. Goodbye!')


a = 10

while a >= 0:
    print(a, end = ' ')
    a -= 1


r = 0
s = 0

while r < 10:
    s = 0
    while s < 5:
        print(f'{r}, {s} ')
        s += 1
    r += 1


for r in range(10):
    for s in range(5):
        print(f'{r}, {s} ')


fruits = ['apple', 'cherry', 'strawberry', 'mango']
numbers = [20, 20, 40, 50, 60]

for x in fruits:
    print (x)

print()    
for number in numbers:
    print(number)
print()    
fruits.append('banana')
print(fruits)

print()
for fruit in fruits:
    print(fruit, end =' ')