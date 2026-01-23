"""
Day 4: Loops Knowledge Check
Date: January 23, 2026
Purpose: Assess current loop knowledge and identify gaps

Instructions:
- Answer each question by writing code
- Be honest about what you know/don't know
- This helps identify what to focus on
"""

print("=" * 60)
print("DAY 4: LOOPS KNOWLEDGE CHECK")
print("=" * 60)
print()

# ============================================================
# QUESTION 1: Basic For Loop
# ============================================================
print("QUESTION 1: Basic For Loop")
print("-" * 40)
print("Task: Loop through a list [1, 2, 3, 4, 5] and print each number")
print("Write your code below:")

# YOUR CODE HERE:
for i in ([1, 2, 3, 4, 5]):
    print(i)
print()

# ============================================================
# QUESTION 2: For Loop with Range
# ============================================================
print("QUESTION 2: For Loop with Range")
print("-" * 40)
print("Task: Print numbers from 0 to 4 using range()")
print("Write your code below:")

# YOUR CODE HERE:
for i in range (5):
    print(i)

print()

# ============================================================
# QUESTION 3: While Loop
# ============================================================
print("QUESTION 3: While Loop")
print("-" * 40)
print("Task: Use a while loop to count from 1 to 5 and print each number")
print("Write your code below:")

# YOUR CODE HERE:
num = 1
while num < 6:
    print(num)
    num += 1

print()

# ============================================================
# QUESTION 4: Loop with Condition
# ============================================================
print("QUESTION 4: Loop with Condition")
print("-" * 40)
print("Task: Loop through [10, 20, 30, 40, 50] and print only numbers greater than 25")
print("Write your code below:")

# YOUR CODE HERE:
for i in ([10, 20, 30, 40, 50]):
    if i > 25:
        print(i)

print()

# ============================================================
# QUESTION 5: Loop with Accumulation
# ============================================================
print("QUESTION 5: Loop with Accumulation")
print("-" * 40)
print("Task: Loop through [1, 2, 3, 4, 5] and calculate the sum")
print("Write your code below:")

# YOUR CODE HERE:
list_sum = 0
for i in ([1, 2, 3, 4, 5]):
    list_sum += i

print(list_sum) #though not mentioned to print, adding it to check
print()

# ============================================================
# QUESTION 6: Loop Through Dictionary
# ============================================================
print("QUESTION 6: Loop Through Dictionary")
print("-" * 40)
print("Task: Loop through dictionary {'a': 1, 'b': 2, 'c': 3} and print each key-value pair")
print("Write your code below:")

# YOUR CODE HERE:
dicts = {'a': 1, 'b': 2, 'c': 3}
for dict in dicts:
    print(f"{dict}: {dicts[dict]}")

print()

# ============================================================
# QUESTION 7: Nested Loops
# ============================================================
print("QUESTION 7: Nested Loops")
print("-" * 40)
print("Task: Create nested loops to print:")
print("  1 2 3")
print("  1 2 3")
print("  1 2 3")
print("(3 rows, each with numbers 1, 2, 3)")
print("Write your code below:")

# YOUR CODE HERE:
for i in range(1, 4):
    rows = " "
    for j in range(1, 4):
        rows += str(j)
        rows += " "
    print(rows)

print()

# ============================================================
# QUESTION 8: Loop Control (break/continue)
# ============================================================
print("QUESTION 8: Loop Control (break/continue)")
print("-" * 40)
print("Task: Loop through [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
print("      Print numbers, but skip 5 (use continue)")
print("      Stop when you reach 8 (use break)")
print("Write your code below:")

# YOUR CODE HERE:
for nums in ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(nums)
    if nums == 5:
        continue
    if nums == 8:
        break
# this is a gap
print()

# ============================================================
# QUESTION 9: Loop with enumerate()
# ============================================================
print("QUESTION 9: Loop with enumerate()")
print("-" * 40)
print("Task: Loop through ['apple', 'banana', 'orange'] and print:")
print("     Index 0: apple")
print("     Index 1: banana")
print("     Index 2: orange")
print("(Use enumerate to get both index and value)")
print("Write your code below:")

# YOUR CODE HERE:
# this is a gap
print()

# ============================================================
# QUESTION 10: List Comprehension
# ============================================================
print("QUESTION 10: List Comprehension")
print("-" * 40)
print("Task: Create a list of squares: [1, 4, 9, 16, 25]")
print("      Using list comprehension: [x**2 for x in range(1, 6)]")
print("      (If you know this, write it. If not, write 'I don't know this yet')")
print("Write your code below:")

# YOUR CODE HERE:
sq_list = []
for x in range(1, 6):
    sq = x ** 2
    sq_list.append(sq)
print(sq_list)
print()
print("=" * 60)
print("KNOWLEDGE CHECK COMPLETE!")
print("=" * 60)
print()
print("After completing, we'll review your answers and identify gaps.")
