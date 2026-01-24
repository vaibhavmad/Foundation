"""
my_math.py - A Simple Module

This is a MODULE (a .py file with functions and variables).
Other files can import this to use its functions.

Think of this as YOUR OWN version of the 'math' module.
"""

# --- Variables (constants) in the module ---
PI = 3.14159
VERSION = "1.0"

# --- Functions in the module ---

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def square(number):
    """Return the square of a number."""
    return number * number
