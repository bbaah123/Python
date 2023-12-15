# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 07:29:02 2023

@author: USER
"""

def is_even(number):
    return number % 2 == 0

def add(x,y):
    return x+y

result = is_even(20)

if(result):
    print('The number is even')
else:
    print('The number is false')
    

#But keys don't have to be strings. They can be numbers:

rankings = {5: 'Finland', 2:'Norway', 3:'Sweden', 7:'Iceland'}

print(rankings[2])



country_ranks = {'Finland': 5, 'Norway':2, 'Sweden': 3, 'Iceland': 7}

print(country_ranks['Norway'])


things_to_remember = {
    0: 'The lowest non-negative number',
    'a dozen': 12,
    'snake eyes': 'a pair of ones',
    13: "a baker's dozen",
    }

print(things_to_remember[0])
print(things_to_remember['a dozen'])

things_to_remember = {}
print(things_to_remember)
things_to_remember[0] = 'the lowest non-negative number'
things_to_remember['a dozen'] = 12

print(things_to_remember)



#Creating a list of dictionaries
customers = [
    {
     'customer id': 0,
     'first name': 'John',
     'last name': 'ogden',
     'address': '301 Arbor Rd.',
     },
    {
     'customer id': 1,
     'first name': 'Ann',
     'last name': 'Sattermeyer',
     'address': 'P.O. Box 1145',
     },
    {
     'customer id': 2,
     'first name': 'Jill',
     'last name': 'Sommers',
     'address': '3 Main St.',
     }
    ]

customer_1 = customers[0]
for key,value in customer_1.items():
    print(key, value)
    
for value in customer_1.values():
    print(value)
    
new_customer = {
    'customer id': 3,
    'first name': 'Joe',
    'last name': 'Biden',
    'address': '111 Main St.',
    }

customers.append(new_customer)

print(customers)

customer_4 = customers[3]
for key,value in customer_4.items():
    print(key, value)
    

#dictionary of lists
"""
customer_29876 qualifies for three discounts, standard, volume, and loyalty. 
He doesn't qualify for a fourth discount, brother-in-law. When he makes a purchase, 
we want to give him the biggest discount he qualifies for, but only that one discount. 
If we give him all the discounts he qualifies for, we'll lose money. 
These are the discounts: brother-in-law – 30% loyalty – 15% volume – 10% standard – 5% 
To find out which discount to give customer_29876, we go through the list of 
discounts named "discounts" in the dictionary customer_29876. We look for each 
discount in turn, starting with the largest one, the brother-in-law discount. 
When we find a discount, the search stops, and that's the discount we apply.
"""

# Define the discounts and customer eligibility using a dictionary of lists
customer_29876 = {
    "discounts": ["brother-in-law", "loyalty", "volume", "standard"],
    "qualifications": {
        "brother-in-law": False,
        "loyalty": True,
        "volume": True,
        "standard": True
    },
    "cities": ['New York', 'London', 'Shanghai', 'Tokyo']
}

print(customer_29876['cities'][2])
print(customer_29876['qualifications']['loyalty'])



discounts = {
    "brother-in-law": 30,
    "loyalty": 15,
    "volume": 10,
    "standard": 5
}

status = customer_29876['qualifications']['brother-in-law']
if(status):
    print('You qualify for the brother-in-law discount')
else:
    print('You do not qualify for the brother-in-law discount')

"""
sorted(discounts.items(), key=lambda x: -x[1])
discounts is a dictionary containing discount types as keys and their corresponding percentage values as values.

.items() is a method used to extract the key-value pairs from the discounts dictionary as a list of tuples. Each tuple contains a discount type and its percentage.

key=lambda x: -x[1] is a key function used to specify the sorting criterion. It's a lambda function that takes each tuple (x) and returns the negative of the second element of the tuple (x[1]), which is the percentage value.

sorted() is a built-in Python function that sorts a sequence (in this case, a list of tuples) based on the specified key function.
"""