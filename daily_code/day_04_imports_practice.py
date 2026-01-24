"""
Day 4: Imports Practice - Importing Your Own Module

This file imports functions from my_math.py (our custom module).
This shows you how imports work "behind the scenes".

When Python sees: import my_math
It looks for: my_math.py in the same folder
Then loads all the code from that file
"""

# --- Method 1: import module_name (use as module.function) ---
import my_math

# Use functions with module prefix
result1 = my_math.add(10, 5)
print("my_math.add(10, 5) =", result1)

result2 = my_math.subtract(20, 8)
print("my_math.subtract(20, 8) =", result2)

# Access variables from module
print("my_math.PI =", my_math.PI)
print("my_math.VERSION =", my_math.VERSION)

# --- Method 2: from module import thing (use directly) ---
from my_math import multiply, square

# Use functions directly (no module prefix)
result3 = multiply(4, 7)
print("multiply(4, 7) =", result3)

result4 = square(9)
print("square(9) =", result4)

# --- Method 3: Import everything (not recommended, but works) ---
from my_math import divide

result5 = divide(100, 4)
print("divide(100, 4) =", result5)

result6 = divide(10, 0)  # Test error handling
print("divide(10, 0) =", result6)
