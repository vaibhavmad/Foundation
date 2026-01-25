"""
Day 5: Control Flow Knowledge Check
Date: January 24, 2026
Purpose: Assess current control flow knowledge (if/elif/else) and identify gaps

Instructions:
- Answer each question by writing code
- Be honest about what you know/don't know
- This helps identify what to focus on
"""

print("=" * 60)
print("DAY 5: CONTROL FLOW KNOWLEDGE CHECK")
print("=" * 60)
print()

# ============================================================
# QUESTION 1: Basic If Statement
# ============================================================
print("QUESTION 1: Basic If Statement")
print("-" * 40)
print("Task: Write an if statement that prints 'Positive' if the variable 'num' is greater than 0.")
print("      (Assume num = 5)")
print("Write your code below:")

num = 5
# YOUR CODE HERE:
if num > 0:
    print("Positive")

print()

# ============================================================
# QUESTION 2: If / Else
# ============================================================
print("QUESTION 2: If / Else")
print("-" * 40)
print("Task: Write logic that prints 'Adult' if 'age' is >= 18, and 'Minor' otherwise.")
print("      (Assume age = 16)")
print("Write your code below:")

age = 16
# YOUR CODE HERE:
if age >= 18:
    print("Adult")
else:
    print("Minor")

print()

# ============================================================
# QUESTION 3: If / Elif / Else
# ============================================================
print("QUESTION 3: If / Elif / Else")
print("-" * 40)
print("Task: Write logic for a traffic light:")
print("      - If color is 'red', print 'Stop'")
print("      - If color is 'yellow', print 'Slow down'")
print("      - If color is 'green', print 'Go'")
print("      - Otherwise, print 'Unknown signal'")
print("      (Assume color = 'yellow')")
print("Write your code below:")

color = 'yellow'
# YOUR CODE HERE:
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Slow down")
elif color == "green":
    print("Go")
else:
    print("Unknown signal")

print()

# ============================================================
# QUESTION 4: Comparison Operators
# ============================================================
print("QUESTION 4: Comparison Operators")
print("-" * 40)
print("Task: Check if 'a' is equal to 'b'. If yes, print 'Equal'.")
print("      Check if 'a' is NOT equal to 'b'. If yes, print 'Not Equal'.")
print("      (Assume a = 10, b = 10)")
print("Write your code below:")

a = 10
b = 10
# YOUR CODE HERE:
if a == b:
    print("Equal")
else:
    print("NOT Equal")

print()

# ============================================================
# QUESTION 5: Boolean Logic (and)
# ============================================================
print("QUESTION 5: Boolean Logic (and)")
print("-" * 40)
print("Task: Print 'Access Granted' ONLY if 'is_admin' is True AND 'is_logged_in' is True.")
print("      (Assume is_admin = True, is_logged_in = True)")
print("Write your code below:")

is_admin = True
is_logged_in = True
# YOUR CODE HERE:
if is_admin and is_logged_in:
    print("Access Granted")

print()

# ============================================================
# QUESTION 6: Boolean Logic (or)
# ============================================================
print("QUESTION 6: Boolean Logic (or)")
print("-" * 40)
print("Task: Print 'Discount Applied' if 'is_student' is True OR 'is_senior' is True.")
print("      (Assume is_student = False, is_senior = True)")
print("Write your code below:")

is_student = False
is_senior = True
# YOUR CODE HERE:
if is_student or is_senior:
    print("Discount Applied")

print()

# ============================================================
# QUESTION 7: Nested If Statements
# ============================================================
print("QUESTION 7: Nested If Statements")
print("-" * 40)
print("Task: Write code that checks if a number is positive.")
print("      IF it is positive, check if it is even or odd.")
print("      Print 'Positive Even' or 'Positive Odd'.")
print("      (Assume number = 4)")
print("Write your code below:")

number = 4
# YOUR CODE HERE:
if number > 0:
    if number % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

print()

# ============================================================
# QUESTION 8: Truthiness (Implicit Booleans)
# ============================================================
print("QUESTION 8: Truthiness")
print("-" * 40)
print("Task: Write an if statement that checks the list 'items'.")
print("      If the list is NOT empty, print 'List has items'.")
print("      If the list IS empty, print 'List is empty'.")
print("Write your code below:")

items = ["apple"]
# YOUR CODE HERE:
if items:
    print("List has items")
else:
    print("List is empty")

print()

# ============================================================
# QUESTION 9: Logical NOT
# ============================================================
print("QUESTION 9: Logical NOT")
print("-" * 40)
print("Task: Use the 'not' operator.")
print("      If 'is_raining' is NOT True, print 'Go outside'.")
print("      (Assume is_raining = False)")
print("Write your code below:")

is_raining = False
# YOUR CODE HERE:
if not is_raining:
    print("Go outside")

print()

# ============================================================
# QUESTION 10: Combining It All (Mini-App)
# ============================================================
print("QUESTION 10: Mini-App")
print("-" * 40)
print("Task: Create a simple password checker.")
print("      - If password length is less than 6, print 'Too short'")
print("      - If password is exactly 'python123', print 'Correct!'")
print("      - Otherwise, print 'Wrong password'")
print("      (Check logic with password = 'code')")
print("Write your code below:")

password = "code"
# YOUR CODE HERE:
if len(password) < 6:
    print("Too short")
elif password == "python123":
    print("Correct!")
else:
    print("Wrong password")

print()
print("=" * 60)
print("KNOWLEDGE CHECK COMPLETE!")
print("=" * 60)
print()
print("After completing, we'll review your answers and identify gaps.")
