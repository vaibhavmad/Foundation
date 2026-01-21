"""
Foundation Day 2 - Lists Practice
Date: January 21, 2026
Goal: Understand and practice Python lists

Instructions:
- Read each section
- Write the code yourself (don't copy-paste from comments)
- Run the file to see results: python daily_code/day_02_lists_practice.py
- Experiment and break things to learn!
"""

print("=" * 50)
print("FOUNDATION DAY 2 - LISTS PRACTICE")
print("=" * 50)
print()

# ============================================================
# SECTION 1: Creating Lists
# ============================================================
print("SECTION 1: Creating Lists")
print("-" * 30)

# TASK 1.1: Create an empty list called 'my_list'
# SYNTAX: variable_name = []
my_list = []

# TASK 1.2: Create a list of 3 of your favorite foods
# SYNTAX: list_name = ["item1", "item2", "item3"]
# Call it 'favorite_foods'
favorite_foods = ["Cholle kulche", "burgers", "Gulab Jamun"]

# TASK 1.3: Create a list of 5 numbers (any numbers you like)
# Call it 'numbers'
numbers = [1, 2, 3, 4, 5]

# TASK 1.4: Print all three lists
# SYNTAX: print(variable_name)
print(my_list)
print(favorite_foods)
print(numbers)



print()

# ============================================================
# SECTION 2: Accessing Items by Index
# ============================================================
print("SECTION 2: Accessing Items by Index")
print("-" * 30)

# Pre-made list for practice
competitors = ["Competitor A", "Competitor B", "Competitor C", "Competitor D", "Competitor E"]

# TASK 2.1: Print the FIRST competitor (index 0)
# SYNTAX: list_name[index]
print(competitors[0])

# TASK 2.2: Print the THIRD competitor (index 2)
print(competitors[2])

# TASK 2.3: Print the LAST competitor (index 4)
print(competitors[-1])

# TASK 2.4: What happens if you try index 10? (Uncomment line below to test)
# print(competitors[10])  # This will cause an error! Try it, read the error, then comment it back
print("IndexError: list index out of range")
print()

# ============================================================
# SECTION 3: Modifying Lists
# ============================================================
print("SECTION 3: Modifying Lists")
print("-" * 30)

# Pre-made list
article_titles = ["Title 1", "Title 2", "Title 3"]

# TASK 3.1: Print the original list
print(f"Original List: {article_titles}")


# TASK 3.2: Change "Title 2" to "Shilajit Benefits"
# SYNTAX: list_name[index] = "new value"
article_titles[1] = "Shilajit Benefits"


# TASK 3.3: Print the modified list
print(f"Modified List: {article_titles}")

print()
# ============================================================
# SECTION 4: Adding Items to Lists
# ============================================================
print("SECTION 4: Adding Items")
print("-" * 30)

# Start with empty list
keywords = []
print("Starting list:", keywords)

# TASK 4.1: Add "shilajit" to the list
# SYNTAX: list_name.append("item")
keywords.append("shilajit")

# TASK 4.2: Add "benefits" to the list
keywords.append("benefits")

# TASK 4.3: Add "dosage" to the list
keywords.append("dosage")

# TASK 4.4: Print the final list
print(f"Keywords: {keywords}")

print()
# ============================================================
# SECTION 5: Removing Items from Lists
# ============================================================
print("SECTION 5: Removing Items")
print("-" * 30)

# Pre-made list
urls = ["url1.com", "url2.com", "spam.com", "url3.com"]
print("Original:", urls)

# TASK 5.1: Remove "spam.com" from the list
# SYNTAX: list_name.remove("item")
urls.remove("spam.com")

# TASK 5.2: Print the cleaned list
print(f"Cleaner URLs: {urls}")

print()

# ============================================================
# SECTION 6: List Length
# ============================================================
print("SECTION 6: List Length")
print("-" * 30)

# Pre-made lists
small_list = ["A", "B"]
medium_list = ["A", "B", "C", "D", "E"]
large_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# TASK 6.1: Print how many items are in small_list
# SYNTAX: len(list_name)
# Example: print(len(small_list))
count_small_list = len(small_list)
count_medium_list = len(medium_list)
count_large_list = len(large_list)
print(count_small_list)

# TASK 6.2: Print how many items are in medium_list
print(count_medium_list)

# TASK 6.3: Print how many items are in large_list
print(count_large_list)

print()

# ============================================================
# SECTION 7: Real-World Scenario (AI_SEO_Writer)
# ============================================================
print("SECTION 7: Real-World Scenario")
print("-" * 30)

# TASK 7.1: Create a list of 5 competitor URLs (make them up)
# Call it 'competitor_urls'
# Example: "https://competitor1.com/shilajit"
competitor_urls = ["https://competitor1.com/shilajit", "https://competitor2.com/shilajit", 
"https://competitor3.com/shilajit", "https://competitor4.com/shilajit", "https://competitor5.com/shilajit"]


# TASK 7.2: Print how many competitors you have
# SYNTAX: len(competitor_urls)

competitor_count = (len(competitor_urls))
print(competitor_count)

# TASK 7.3: Print the FIRST competitor URL
print(competitor_urls[0])

# TASK 7.4: Print the LAST competitor URL (index 4)
print(competitor_urls[-1])

# TASK 7.5: Add a 6th competitor URL
competitor_urls.append("https://competitor6.com/shilajit")

# TASK 7.6: Print the updated count
print(competitor_count)

print()

# ============================================================
# SECTION 8: Challenge Problems (Optional)
# ============================================================
print("SECTION 8: Challenge Problems")
print("-" * 30)

# CHALLENGE 8.1: Create a list of 3 article word counts (numbers)
# Then print the MIDDLE one (index 1)
article_word_count = [1100, 1200, 1300]
print(article_word_count[1])

# CHALLENGE 8.2: Create a list with mixed types
# Include: a string, a number, a float, and a boolean
# Example: ["Hello", 42, 3.14, True]
random_items = ["Word", 1, 10.5, False]

# CHALLENGE 8.3: Create a list of your daily learning topics
# Should have: "Python Basics", "Lists", and one more topic you want to learn
daily_learning_topics = ["Python Basics", "Lists", "git"]


print()
print("=" * 50)
print("LISTS PRACTICE COMPLETE!")
print("=" * 50)
print()
print("🎉 Great job! You've practiced:")
print("✅ Creating lists")
print("✅ Accessing items by index")
print("✅ Modifying lists")
print("✅ Adding and removing items")
print("✅ Using len() to count items")
print()
print("Next: Dictionaries (key-value pairs)")
