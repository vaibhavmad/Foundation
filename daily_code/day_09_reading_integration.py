"""
Foundation Day 9 - Reading Code + Integration
Date: January 30, 2026
Goal: Read and understand existing code; combine concepts (data structures, functions, loops, JSON, error handling)

Instructions:
- Section 1: Read the code snippet, then in comments write what it does and what the output is. Run to check.
- Section 2: Write a short integration script using multiple concepts (see task).
- Run: python3 daily_code/day_09_reading_integration.py
"""
import json

print("=" * 50)
print("FOUNDATION DAY 9 - READING CODE + INTEGRATION")
print("=" * 50)
print()

# ============================================================
# SECTION 1: Read this code
# ============================================================
print("SECTION 1: Read this code")
print("-" * 30)

# Below is a short snippet. BEFORE running:
# 1. In comments, write in your own words: what does this code do?
# 2. In comments, write: what do you think the output will be?
# Then run the file and see if you were right.

def double(x):
    return x * 2

numbers = [1, 2, 3]
result = []
for n in numbers:
    result.append(double(n))
print("Output:", result)

# YOUR COMMENTS HERE:
# What does this code do?
#a function is created - double, which intakes parameter x, then two lists are create [1, 2, 3] & [], numbers and result respectively. 
# then a loop runs, doubles each item in numbers list, adds those to result
# What is the output?
#[2, 4, 6]

print()

# ============================================================
# SECTION 2: Integration — combine concepts
# ============================================================
print("SECTION 2: Integration")
print("-" * 30)

# TASK: Write a short script that uses ALL of the following:
# - A data structure (list or dict)
# - A function (e.g. one that takes data and returns a formatted string)
# - A loop (over the data)
# - JSON: use a JSON string, parse it with json.loads
# - try/except: wrap the json.loads in try/except; if it fails, print a short error message
#
# Example idea: A JSON string of 2–3 "products" (each with "name" and "price").
# Parse it, loop over the products, and use a function to format each as one line (e.g. "Product: X, Price: Y").
# If parsing fails, print "Invalid JSON."
#
# Write your code below. No hints — use what you learned on Days 1–8.

# Your integration script:

product_string = '[{"product_name": "Samsung Mobile", "product_storage_GB": "128", "is_available": true}, {"product_name": "Micromax Mobile", "product_storage_GB": "256", "is_available": false}, {"product_name": "Apple Mobile", "product_storage_GB": "512", "is_available": true}]'
try:
    product_list = json.loads(product_string)
except:
    print("Invalid Json")
    product_list = []

# write a function to check if item is available, if available, return 
def product_check(item_name, item_status):
    if item_status:
        return f"{item_name} is available"
    else:
        return f"{item_name} is not available" 

# run the above function in a loop and output of the result and print if item is available or not

for key in product_list:
    status = product_check(key["product_name"], key["is_available"],)
    print(status)


print()
print("Day 9 practice complete.")