"""
Foundation Day 7 - String Formatting + JSON Practice
Date: January 29, 2026
Goal: Understand f-strings, .format(), and JSON (loads/dumps, load/dump with files)

Instructions:
- Read each section
- Write the code yourself (don't copy-paste from comments)
- Run: python3 daily_code/day_07_string_formatting_json_practice.py
"""
import json

print("=" * 50)
print("FOUNDATION DAY 7 - STRING FORMATTING + JSON")
print("=" * 50)
print()

# ============================================================
# SECTION 1: f-strings (quick recap)
# ============================================================
print("SECTION 1: f-strings")
print("-" * 30)

# TASK 1.1: Create variables name = "Alice", age = 30
# Use an f-string to create: "My name is Alice and I am 30 years old."
# Print the result
name, age = "Alice", 30
result = f"My name is {name} and I am {age} years old."

print(result)

# TASK 1.2: Create a list [10, 20, 30]. Use an f-string to print "The list has 3 items and the first is 10."
list_is = [10, 20, 30]

print(f"The list has {len(list_is)} items and the first is {list_is[0]}")

print()

# ============================================================
# SECTION 2: .format() method
# ============================================================
print("SECTION 2: .format() method")
print("-" * 30)

# TASK 2.1: Using .format(), create the string "Hello, Alice! You are 30 years old."
# Use variables name = "Alice", age = 30
# Format: "Hello, {}! You are {} years old.".format(name, age)
# Print the result
print("Hello, {}! You are {} years old.".format(name, age))


# TASK 2.2: Using .format() with named placeholders
# Create: "Item: apple, Price: 1.50"
# Use: "Item: {item}, Price: {price}".format(item="apple", price=1.50)
# Print the result

print("Item: {item}, Price: {price}".format(item = "apple", price = 1.50))

print()

# ============================================================
# SECTION 3: JSON - loads and dumps (in-memory)
# ============================================================
print("SECTION 3: JSON loads and dumps")
print("-" * 30)

# TASK 3.1: Import json at the top if not already
# Create a Python dictionary: {"name": "Alice", "age": 30}
# Use json.dumps() to convert it to a JSON string
# Print the JSON string
dict_1 = {"name": "Alice", "age": 30}
json_string = json.dumps(dict_1)
print(json_string)
# TASK 3.2: Take a JSON string: '{"city": "Mumbai", "country": "India"}
# Use json.loads() to convert it to a Python dictionary
# Print the dictionary and then print the value of the key "city"

new_string = '{"city": "Mumbai", "country": "India"}'
dict_1 = json.loads(new_string)
print(dict_1)

print()

# ============================================================
# SECTION 4: JSON - load and dump (with files)
# ============================================================
print("SECTION 4: JSON with files")
print("-" * 30)

# TASK 4.1: Create a dictionary {"title": "My Note", "content": "Hello JSON"}
# Use json.dump() to write it to a file called "data.json"
# Open the file in write mode, then json.dump(my_dict, file)
dict_4 = {"title": "My Note", "content": "Hello JSON"}
with open("data.json", "w") as file:
    json.dump(dict_4, file)

# TASK 4.2: Use json.load() to read "data.json" back into a Python variable
# Open the file in read mode, then data = json.load(file)
# Print the variable and print data["title"]
with open("data.json", "r") as file:
    content  = json.load(file)

print(content["title"])

print()

# ============================================================
# SECTION 5: Quick integration
# ============================================================
print("SECTION 5: Quick integration")
print("-" * 30)

# TASK 5.1: Write a function that takes a dictionary and a filename
# Function name: save_to_json
# Use json.dump() to write the dictionary to the file
# Call with: save_to_json({"a": 1, "b": 2}, "output.json")
def save_to_json(dict, file_name):
    with open(file_name, "w") as file:
        json.dump(dict, file)
save_to_json({"a": 1, "b": 2}, "output.json")
    
# TASK 5.2: Write a function that takes a filename and returns the data
# Function name: load_from_json
# Use json.load() to read the file and return the result
# Call with: load_from_json("output.json") and print the result
def load_from_json(file_name):
    with open(file_name, "r") as file:
        content = json.load(file)
    return content

print(load_from_json("output.json"))


print()
print("=" * 50)
print("DAY 7 PRACTICE COMPLETE!")
print("=" * 50)
