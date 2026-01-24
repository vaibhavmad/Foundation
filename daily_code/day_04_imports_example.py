"""
Day 4: Imports - Simple Examples
Focus: import X, from X import Y, using imported functions

Python ships with "modules" (bundles of useful functions).
You bring them into your file with import.
"""

# --- 1. import module_name (use as module.function) ---
import math
import my_math

# Use: module_name.function_name(...)
sqrt_16 = math.sqrt(16)
print("math.sqrt(16) =", sqrt_16)
print("math.pi =", math.pi)

# --- 2. from module import thing (use directly) ---
from random import randint

# Use: thing(...) — no module prefix
roll = randint(1, 6)
print("randint(1, 6) =", roll)


cube_of = my_math.cube(4)
print(cube_of)
