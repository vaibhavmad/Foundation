"""
Foundation Day 6 - Error Handling Practice
Date: January 29, 2026
Goal: Understand and practice try/except blocks, handling errors gracefully

Instructions:
- Read each section
- Write the code yourself (don't copy-paste from comments)
- Run the file to see results: python3 daily_code/day_06_error_handling_practice.py
- Experiment and break things to learn!
"""


print("=" * 50)
print("FOUNDATION DAY 6 - ERROR HANDLING PRACTICE")
print("=" * 50)
print()

# ============================================================
# SECTION 1: Basic try/except
# ============================================================
print("SECTION 1: Basic try/except")
print("-" * 30)

# TASK 1.1: Write a try/except block that tries to divide 10 by 0
# In the except block, print "Error: Cannot divide by zero!"
try:
    result = 10/0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# TASK 1.2: Write a try/except block that tries to convert the string "hello" to an integer
# In the except block, print "Error: Cannot convert to integer!"
try:
    int("hello")
except ValueError:
    print("Error: Cannot convert to integer!")


# TASK 1.3: Write a try/except block that tries to access index 10 of a list [1, 2, 3]
# In the except block, print "Error: Index out of range!"
list = [1, 2, 3]
try:
    print(list[10])
except IndexError:
    print("Error: Index out of range!")


print()

# ============================================================
# SECTION 2: Specific Error Types
# ============================================================
print("SECTION 2: Specific Error Types")
print("-" * 30)

# TASK 2.1: Write a try/except block with multiple specific except blocks
# Try: 10 / 0
# First except: Catch ZeroDivisionError, print "Division error!"
# Second except: Catch ValueError, print "Value error!"
# Third except: Catch all other errors, print "Some other error!"
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division error!")
except ValueError:
    print("Value error!")
except:
    print("Some other error!")


# TASK 2.2: Write a function that processes user input with specific error handling
# Function name: process_user_number
# Parameter: user_input (a string)
# Try: Convert user_input to int, then divide 100 by that number
# If ValueError: return "Error: '[user_input]' is not a valid number!"
# If ZeroDivisionError: return "Error: Cannot divide by zero!"
# else: return f"Result: [result]"
# Call with: process_user_number("5") and process_user_number("hello") and process_user_number("0")
def process_user_number(user_input):
    try:
        result = 100 / int(user_input)
    except ValueError: 
        return f"Error: '{user_input}' is not a valid number!"
    except ZeroDivisionError: 
        return "Error: Cannot divide by zero!"
    else:
        return f"Result: {result}"

result_1 = process_user_number("5")
result_2 = process_user_number("hello")
result_3 = process_user_number("0")

print(result_1)
print(result_2)
print(result_3)

# TASK 2.3: Write a try/except block that handles different errors differently
# Try: int("hello") / 0
# First except: Catch ValueError, print "Invalid input - not a number!"
# Second except: Catch ZeroDivisionError, print "Cannot divide by zero!"
# Note: This will catch ValueError first (since int() fails before division)
try:
    result = int("hello")/0
except ValueError:
    print("Invalid input - not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


# TASK 2.4: Write a try/except block that demonstrates catching the right error
# Try: Access a dictionary key that doesn't exist: {"name": "Alice"}["age"]
# Catch KeyError specifically and print "Key 'age' not found in dictionary!"
# Then try: Access a list index that doesn't exist: [1, 2, 3][10]
# Catch IndexError specifically and print "Index 10 out of range for list!"
# Note: These are two separate try/except blocks
dict = {
    "name": "Alice"
}
try:
    result = dict["age"]
except KeyError:
    print("Key 'age' not found in dictionary!")

list = [1, 2, 3]
try:
    result = list[10]
except IndexError:
    print("Index 10 out of range for list!")

print()

# ============================================================
# SECTION 3: File Error Handling
# ============================================================
print("SECTION 3: File Error Handling")
print("-" * 30)

# TASK 3.1: Write a try/except block that tries to open a file called "nonexistent.txt"
# Catch FileNotFoundError and print "File not found!"


# TASK 3.2: Write a function that safely reads a file
# Function name: safe_read_file
# Parameter: filename
# Try: Open and read the file
# If FileNotFoundError: return "File not found: [filename]"
# else: return the file content
# Call with: safe_read_file("test_write.txt") and safe_read_file("nonexistent.txt")


print()

# ============================================================
# SECTION 4: else and finally Clauses
# ============================================================
print("SECTION 4: else and finally Clauses")
print("-" * 30)

# TASK 4.1: Write a try/except/else block
# Try: Convert "42" to integer
# If ValueError: print "Invalid number!"
# else: print "Success! Number is: [the number]"


# TASK 4.2: Write a try/except/finally block
# Try: 10 / 0
# If ZeroDivisionError: print "Division error!"
# finally: print "This always runs!"


# TASK 4.3: Write a try/except/finally block for file operations
# Try: Open "test_write.txt" in read mode
# If FileNotFoundError: print "File not found!"
# finally: print "File operation completed!"


print()

# ============================================================
# SECTION 5: Getting Error Details
# ============================================================
print("SECTION 5: Getting Error Details")
print("-" * 30)

# TASK 5.1: Write a try/except block that captures the error message
# Try: 10 / 0
# Catch ZeroDivisionError as 'e' and print "Error: [error message]"


# TASK 5.2: Write a try/except block that captures FileNotFoundError details
# Try: open("nonexistent.txt")
# Catch FileNotFoundError as 'e' and print "FileError: [error message]"


print()

# ============================================================
# SECTION 6: Quick Integration - Functions + Error Handling
# ============================================================
print("SECTION 6: Quick Integration")
print("-" * 30)

# TASK 6.1: Write a function that safely gets a value from a dictionary
# Function name: safe_get_value
# Parameters: my_dict, key
# Try: Access my_dict[key]
# If KeyError: return "Key '[key]' not found in dictionary!"
# else: return the value
# Call with: safe_get_value({"name": "Alice"}, "name") and safe_get_value({"name": "Alice"}, "age")


# TASK 6.2: Write a function that safely processes a list of strings as numbers
# Function name: safe_process_numbers
# Parameter: number_strings (a list of strings like ["10", "20", "thirty", "40"])
# Create an empty list called 'numbers'
# Loop through each string, try to convert to int
# If ValueError: Continue to next item (skip invalid strings)
# else: Append converted number to 'numbers'
# Return the sum of 'numbers'
# Call with: safe_process_numbers(["10", "20", "thirty", "40"])


print()

print("=" * 50)
print("ERROR HANDLING PRACTICE COMPLETE!")
print("=" * 50)
