"""
Foundation Day 4 - Imports Practice
Date: January 24, 2026
Goal: Test your understanding of Python imports

Instructions:
- Read each section
- Write the code yourself (don't copy-paste from comments)
- Run the file to see results: python3 day_04_imports_practice.py
- Use the my_math.py module you created earlier
- Experiment and break things to learn!
"""

print("=" * 50)
print("FOUNDATION DAY 4 - IMPORTS PRACTICE")
print("=" * 50)
print()

# ============================================================
# SECTION 1: Basic Import (import module_name)
# ============================================================
print("SECTION 1: Basic Import (import module_name)")
print("-" * 30)

# TASK 1.1: Import the math module
# (Write: import math)
import math
# TASK 1.2: Use math.sqrt() to calculate the square root of 25
# Store the result in a variable called 'result1'
# Print the result
result1 = math.sqrt(25)
print(result1)
# TASK 1.3: Use math.pi to get the value of pi
# Store it in a variable called 'pi_value'
# Print the result
pi_value = math.pi
print(pi_value)
print()

# ============================================================
# SECTION 2: From Import (from module import thing)
# ============================================================
print("SECTION 2: From Import (from module import thing)")
print("-" * 30)

# TASK 2.1: Import randint from the random module
# (Write: from random import randint)
from random import randint

# TASK 2.2: Use randint(1, 10) to generate a random number between 1 and 10
# Store it in a variable called 'random_num'
# Print the result
random_num = randint(1, 10)
print(random_num)

# TASK 2.3: Import floor from the math module
# (Write: from math import floor)
from math import floor

# TASK 2.4: Use floor(3.7) to round down 3.7
# Store it in a variable called 'rounded_down'
# Print the result
rounded_down = floor(3.7)
print(rounded_down)

print()

# ============================================================
# SECTION 3: Importing Your Own Module
# ============================================================
print("SECTION 3: Importing Your Own Module")
print("-" * 30)

# TASK 3.1: Import the my_math module
# (Write: import my_math)
import my_math

# TASK 3.2: Use my_math.add(15, 20) to add 15 and 20
# Store the result in a variable called 'sum_result'
# Print the result
sum_result = my_math.add(15, 20)
print(sum_result)

# TASK 3.3: Use my_math.multiply(6, 7) to multiply 6 and 7
# Store the result in a variable called 'product'
# Print the result
product = my_math.multiply(6, 7)
print(product)

# TASK 3.4: Access my_math.PI to get the PI constant
# Store it in a variable called 'my_pi'
# Print the result
my_pi = my_math.PI
print(my_pi)
print()

# ============================================================
# SECTION 4: From Import with Your Module
# ============================================================
print("SECTION 4: From Import with Your Module")
print("-" * 30)

# TASK 4.1: Import square from my_math module
# (Write: from my_math import square)
from my_math import square

# TASK 4.2: Use square(5) to calculate 5 squared
# Store it in a variable called 'five_squared'
# Print the result (should be 25)
five_squared = square(5)
print(five_squared)

# TASK 4.3: Import cube from my_math module
# (Write: from my_math import cube)
from my_math import cube

# TASK 4.4: Use cube(3) to calculate 3 cubed
# Store it in a variable called 'three_cubed'
# Print the result (should be 27)
three_cubed = cube(3)
print(three_cubed)

print()

# ============================================================
# SECTION 5: Multiple Imports
# ============================================================
print("SECTION 5: Multiple Imports")
print("-" * 30)

# TASK 5.1: Import both add and subtract from my_math in one line
# (Write: from my_math import add, subtract)
from my_math import add, subtract

# TASK 5.2: Use add(100, 50) and store in 'result_a'
# Use subtract(100, 50) and store in 'result_b'
# Print both results
result_a = add(100, 50)
result_b = subtract(100, 50)
print(result_a)
print(result_b)

print()

# ============================================================
# SECTION 6: Using Imported Functions in Calculations
# ============================================================
print("SECTION 6: Using Imported Functions in Calculations")
print("-" * 30)

# TASK 6.1: Import divide from my_math
# (Write: from my_math import divide)
from my_math import divide

# TASK 6.2: Calculate: divide(50, 2) and store in 'division_result'
# Print the result
division_result = divide(50, 2)
print(division_result)

# TASK 6.3: Calculate: divide(10, 0) and store in 'error_result'
# Print the result (should show error message)
error_result = divide(10, 0)
print(error_result)

print()

# ============================================================
# SECTION 7: Combining Built-in and Custom Imports
# ============================================================
print("SECTION 7: Combining Built-in and Custom Imports")
print("-" * 30)

# TASK 7.1: You already have math imported (from Section 1)
# You already have square imported from my_math (from Section 4)
# Calculate: math.sqrt(square(4))
# Explanation: square(4) = 16, then sqrt(16) = 4
# Store in 'combined_result'
# Print the result
combined_result = math.sqrt(square(4))
print(combined_result)

print()

# ============================================================
# SECTION 8: Challenge - Create a Function Using Imports
# ============================================================
print("SECTION 8: Challenge - Create a Function Using Imports")
print("-" * 30)

# TASK 8.1: Define a function called 'calculate_area' that takes one parameter 'radius'
# Inside the function:
#   - Use my_math.multiply() to calculate: radius * radius
#   - Use math.pi to get pi
#   - Use my_math.multiply() again to multiply the two results
#   - Return the final result
# Formula: area = pi * radius * radius
def calculate_area(radius):
    r_squared = my_math.multiply(radius, radius)
    return my_math.multiply(r_squared, math.pi)

# TASK 8.2: Call calculate_area(5) and store in 'circle_area'
# Print the result (should be approximately 78.54)
circle_area = calculate_area(5)
print(circle_area)
print()

# ============================================================
# SECTION 9: Challenge - Import and Use Multiple Functions
# ============================================================
print("SECTION 9: Challenge - Import and Use Multiple Functions")
print("-" * 30)

# TASK 9.1: Import add, subtract, multiply, and divide from my_math in one line
# (Write: from my_math import add, subtract, multiply, divide)
from my_math import add, subtract, multiply, divide

# TASK 9.2: Create a variable 'num1' = 20
# Create a variable 'num2' = 5
num1, num2 = 20, 5

# TASK 9.3: Calculate all four operations:
#   - add(num1, num2) → store in 'addition'
#   - subtract(num1, num2) → store in 'subtraction'
#   - multiply(num1, num2) → store in 'multiplication'
#   - divide(num1, num2) → store in 'division'
addition = add(num1, num2)
subtraction = subtract(num1, num2)
multiplication = multiply(num1, num2)
division = divide(num1, num2)

# TASK 9.4: Print all four results in this format:
#   "20 + 5 = [result]"
#   "20 - 5 = [result]"
#   "20 * 5 = [result]"
#   "20 / 5 = [result]"
print(f"20 + 5 = {addition}")
print(f"20 - 5 = {subtraction}")
print(f"20 * 5 = {multiplication}")
print(f"20 / 5 = {division}")

print()

print("=" * 50)
print("PRACTICE COMPLETE!")
print("=" * 50)
print()
print("Review your code and make sure:")
print("1. All imports are at the top of each section")
print("2. All results are stored in variables")
print("3. All results are printed")
print("4. The file runs without errors")
