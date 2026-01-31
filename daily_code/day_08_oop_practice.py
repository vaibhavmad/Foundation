"""
Foundation Day 8 - Classes/OOP Practice
Date: January 30, 2026
Goal: Define a class, create objects, use attributes and methods

Instructions:
- Read each section
- Write the code yourself (don't copy-paste from comments)
- Run: python3 daily_code/day_08_oop_practice.py
"""


print("=" * 50)
print("FOUNDATION DAY 8 - CLASSES/OOP PRACTICE")
print("=" * 50)
print()

# ============================================================
# SECTION 1: Define a class with __init__ and attributes
# ============================================================
print("SECTION 1: Define a class with __init__ and attributes")
print("-" * 30)

# TASK 1.1: Define a class called Person that has name and age.
# Create one object with name "Alice" and age 30.
# Print the object's name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)

print(person1.name)
print(person1.age)

print()

# ============================================================
# SECTION 2: Add a method to the class
# ============================================================
print("SECTION 2: Add a method to the class")
print("-" * 30)

# TASK 2.1: Add a method to Person that prints a greeting with the person's name.
# Call it on the object you created.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello, {self.name}")
person1 = Person("Alice", 30)
person1.greeting()

# TASK 2.2: Add a method that returns a string with the person's name and age.
# Call it and print the result.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello, {self.name}")

    def identity(self):
        return f"Name: {self.name}, Age: {self.age}"

person1 = Person("Alice", 30)

print(person1.identity())
print()

# ============================================================
# SECTION 3: Create multiple objects
# ============================================================
print("SECTION 3: Create multiple objects")
print("-" * 30)

# TASK 3.1: Create a second Person object with name "Bob" and age 25.
# Print its name and age, and call the greeting method.
person2 = Person("Bob", 25)
print(person2.name)
print(person2.age)

person2.greeting()

print()

# ============================================================
# SECTION 4: Another class (Product)
# ============================================================
print("SECTION 4: Another class (Product)")
print("-" * 30)

# TASK 4.1: Define a class called Product with name and price.
# Add a method that prints the product name and price (e.g. "Notebook: Rs 50").
# Create two product objects (e.g. Notebook 50, Pen 10) and call the method on each.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def details(self):
        print(f"{self.name}: Rs {self.price}")

product1 = Product("Notebook", 50)
product2 = Product("Pen", 10)

product1.details()
product2.details()

print()
print("=" * 50)
print("DAY 8 OOP PRACTICE COMPLETE!")
print("=" * 50)
