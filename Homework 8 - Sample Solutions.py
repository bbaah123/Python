# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 08:20:13 2024

@author: USER
"""

# Problem 1: Multiple Inheritance and Method Resolution Order
class Animal:
    def __init__(self):
        print("Animal's constructor")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal's constructor")

class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("Bird's constructor")

class Platypus(Mammal, Bird):
    def __init__(self):
        super().__init__()
        print("Platypus's constructor")

# Test the MRO
perry = Platypus()

# Problem 2: Global vs Local Variables
global_var = 10

def modify_variable():
    local_var = global_var
    local_var += 5
    print("Inside function:", local_var)

modify_variable()
print("Outside function:", global_var)

def modify_global_variable():
    global global_var
    global_var += 5

modify_global_variable()
print("After modifying global variable:", global_var)

# Problem 3: Set Operations
set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 60, 70}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference set_a - set_b:", set_a - set_b)
print("Difference set_b - set_a:", set_b - set_a)
print("Symmetric Difference:", set_a ^ set_b)

# Problem 4: Tuple Manipulations
tuple_a = (100, 200, 300)
print("First element:", tuple_a[0])
print("Last element:", tuple_a[-1])

x, y, z = tuple_a
print("Unpacked:", x, y, z)

new_tuple = tuple_a + (400, 500)
print("Concatenated tuple:", new_tuple)

repeated_tuple = tuple_a * 2
print("Repeated tuple:", repeated_tuple)

# Problem 5: Class Attributes and Instance Attributes
class Vehicle:
    category = 'Transport'

    def __init__(self, name):
        self.name = name

    def display_info(self):
        return f"Category: {Vehicle.category}, Name: {self.name}"

car = Vehicle("Car")
print(car.display_info())

# Problem 6: Exception Handling in Inheritance
class ParentA:
    def risky_method(self):
        raise NotImplementedError("This method is not implemented")

class ParentB:
    def risky_method(self):
        print("Safe method in ParentB")

class Child(ParentA, ParentB):
    def use_risky_method(self):
        try:
            self.risky_method()
        except NotImplementedError as e:
            print(f"Caught an exception: {e}")

child_instance = Child()
child_instance.use_risky_method()
