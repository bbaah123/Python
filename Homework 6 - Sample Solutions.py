# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:28:48 2023

@author: USER
"""

# Problem 1: Dictionary Access and Modification
# You have a dictionary representing information about a customer:

customer_info = {
    'customer_id': 12345,
    'first_name': 'Alice',
    'last_name': 'Smith',
    'email': 'alice@example.com'
}

# a. Print the customer's first name.
print(customer_info['first_name'])

# b. Add a new key-value pair to the dictionary: 'phone' with the value '555-1234'.
customer_info['phone'] = '555-1234'

# c. Update the customer's email to 'alice.smith@example.com'.
customer_info['email'] = 'alice.smith@example.com'

# d. Print the customer's last name.
print(customer_info['last_name'])

# Problem 2: Looping Through a Dictionary
# You have a dictionary containing information about several customers:

customers = {
    1: {'name': 'John', 'age': 30},
    2: {'name': 'Jane', 'age': 25},
    3: {'name': 'Bob', 'age': 35}
}

# a. Loop through the `customers` dictionary and print the name and age of each customer.
for customer_id, customer_data in customers.items():
    print(f"Customer ID: {customer_id}")
    print(f"Name: {customer_data['name']}")
    print(f"Age: {customer_data['age']}")
    print()

# Problem 3: Dictionary of Lists
# You have a dictionary of lists representing customer orders:

customer_orders = {
    'customer1': ['product1', 'product2', 'product3'],
    'customer2': ['product2', 'product4'],
    'customer3': ['product1', 'product3', 'product5']
}

# a. Print the list of products that 'customer2' has ordered.
print(customer_orders['customer2'])

# b. Add a new order for 'customer1' with 'product4'.
customer_orders['customer1'].append('product4')

# c. Print the list of products that 'customer1' has ordered after the addition.
print(customer_orders['customer1'])

# Problem 4: Sorting a Dictionary
# You have a dictionary containing product prices:

product_prices = {
    'product1': 10.99,
    'product2': 5.49,
    'product3': 8.75,
    'product4': 12.99
}

# a. Sort the products in ascending order of their prices.
sorted_prices = sorted(product_prices.items(), key=lambda x: x[1])
print(sorted_prices)

# b. Print the product with the highest price.
highest_priced_product = max(product_prices, key=product_prices.get)
print(highest_priced_product)

# Problem 5: Nested Dictionary
# You have a nested dictionary representing a student's grades:

student_grades = {
    'math': {'exam1': 85, 'exam2': 92, 'final': 88},
    'science': {'exam1': 78, 'exam2': 85, 'final': 80}
}

# a. Print the student's math final grade.
print(student_grades['math']['final'])

# b. Print the student's science exam2 grade.
print(student_grades['science']['exam2'])

# Problem 6: More Dictionary Operations
# You have a dictionary containing information about books:

books = {
    'book1': {'title': 'Python Basics', 'author': 'John Doe', 'year': 2020},
    'book2': {'title': 'Data Science Handbook', 'author': 'Jane Smith', 'year': 2019}
}

# a. Add a new book ('book3') with title 'Machine Learning' by 'Bob Johnson' published in 2021.
books['book3'] = {'title': 'Machine Learning', 'author': 'Bob Johnson', 'year': 2021}

# b. Print the title of 'book2'.
print(books['book2']['title'])

# c. Print the author of 'book3'.
print(books['book3']['author'])

# Problem 7: Dictionary Operations and Conditionals
# You have a dictionary representing a customer's discounts:

discounts = {
    'standard': 5,
    'volume': 10,
    'loyalty': 15,
    'brother-in-law': 30
}

customer = {
    'discounts': ['loyalty', 'volume', 'standard'],
    'qualifications': {
        'loyalty': True,
        'volume': True,
        'standard': True,
        'brother-in-law': False
    }
}

# a. Find the highest discount that the customer qualifies for and print it.
highest_discount = max(customer['discounts'], key=lambda x: discounts.get(x, 0))
print(f"Highest Discount: {highest_discount}")

# b. Calculate the discount percentage for the discount found in part (a).
discount_percentage = discounts.get(highest_discount, 0)
print(f"Discount Percentage: {discount_percentage}%")

# c. If the customer qualifies for the 'brother-in-law' discount, print "You qualify for the brother-in-law discount," otherwise print "You do not qualify for the brother-in-law discount."
if customer['qualifications']['brother-in-law']:
    print("You qualify for the brother-in-law discount")
else:
    print("You do not qualify for the brother-in-law discount")
