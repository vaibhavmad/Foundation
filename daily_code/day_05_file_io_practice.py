"""
Foundation Day 5 - File I/O Practice
Date: January 26, 2026
Goal: Understand and practice reading/writing files (manual and with statement)

Instructions:
- Read each section
- Write the code yourself (don't copy-paste from comments)
- Run the file to see results: python3 daily_code/day_05_file_io_practice.py
- Experiment and break things to learn!
"""

print("=" * 50)
print("FOUNDATION DAY 5 - FILE I/O PRACTICE")
print("=" * 50)
print()

# ============================================================
# SECTION 1: Writing Files - Manual Mode (open/close)
# ============================================================
print("SECTION 1: Writing Files - Manual Mode")
print("-" * 30)

# TASK 1.1: Open a file called "manual_write.txt" in write mode
# Store it in a variable called 'file'
file = open("manual_write.txt", "w")

# TASK 1.2: Write "Hello from manual mode!" to the file
file.write("Hello from manual mode!")

# TASK 1.3: Close the file
file.close()

print("✅ File written using manual mode (open/close)")

print()

# ============================================================
# SECTION 2: Reading Files - Manual Mode (open/close)
# ============================================================
print("SECTION 2: Reading Files - Manual Mode")
print("-" * 30)

# TASK 2.1: Open "manual_write.txt" in read mode
file = open("manual_write.txt", "r")

# TASK 2.2: Read all content from the file and store it in a variable called 'content'
content = file.read()

# TASK 2.3: Close the file
file.close()

# TASK 2.4: Print the content you read
print(f"Content read: {content}")

print()

# ============================================================
# SECTION 3: Writing Files - With Statement (Recommended)
# ============================================================
print("SECTION 3: Writing Files - With Statement")
print("-" * 30)

# TASK 3.1: Write "Hello from with statement!" to "with_write.txt" using with statement
with open("with_write.txt", "w") as file:
    file.write("Hello from with statement!")

print("✅ File written using with statement (automatic close)")

print()

# ============================================================
# SECTION 4: Reading Files - With Statement (Recommended)
# ============================================================
print("SECTION 4: Reading Files - With Statement")
print("-" * 30)

# TASK 4.1: Read "with_write.txt" using with statement
with open("with_write.txt", "r") as file:
    content = file.read()

# TASK 4.2: Print the content
print(f"Content read: {content}")

print()

# ============================================================
# SECTION 5: Writing Multiple Lines
# ============================================================
print("SECTION 5: Writing Multiple Lines")
print("-" * 30)

# TASK 5.1: Write three lines to "multi_line.txt" using with statement
# Line 1: "First line"
# Line 2: "Second line"
# Line 3: "Third line"
# TIP: Use file.write() multiple times, or add "\n" for new lines
with open("multi_line.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

print("✅ Multiple lines written")

# TASK 5.2: Read and print the entire file
with open("multi_line.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

print()

# ============================================================
# SECTION 6: Reading Line by Line - readlines()
# ============================================================
print("SECTION 6: Reading Line by Line (readlines)")
print("-" * 30)

# TASK 6.1: Read "multi_line.txt" using readlines()
# This returns a LIST of lines (each line is a string)
with open("multi_line.txt", "r") as file:
    lines = file.readlines()

# TASK 6.2: Print the lines list (you'll see it's a list)
print(f"Lines as list: {lines}")

# TASK 6.3: Print each line individually using a loop
print("Each line:")
for line in lines:
    print(line.strip())  # .strip() removes the \n at the end

print()

# ============================================================
# SECTION 7: Writing Multiple Lines - writelines()
# ============================================================
print("SECTION 7: Writing Multiple Lines (writelines)")
print("-" * 30)

# TASK 7.1: Create a list of strings (each string is a line)
lines_list = ["Apple\n", "Banana\n", "Orange\n"]

# TASK 7.2: Write all lines at once using writelines()
with open("fruits.txt", "w") as file:
    file.writelines(lines_list)

print("✅ Multiple lines written using writelines()")

# TASK 7.3: Read and print the file to verify
with open("fruits.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

print()

# ============================================================
# SECTION 8: Append Mode - Adding to Existing Files
# ============================================================
print("SECTION 8: Append Mode (Adding to Files)")
print("-" * 30)

# TASK 8.1: Write "Original content" to "append_test.txt" in write mode
with open("append_test.txt", "w") as file:
    file.write("Original content\n")

# TASK 8.2: Append "New content" to the same file using append mode
# Mode "a" = append (adds to end, doesn't overwrite)
with open("append_test.txt", "a") as file:
    file.write("New content\n")

# TASK 8.3: Read and print the entire file
with open("append_test.txt", "r") as file:
    content = file.read()
    print("File content after append:")
    print(content)

print()

# ============================================================
# SECTION 9: Real-World Scenario - Saving Article
# ============================================================
print("SECTION 9: Real-World Scenario - Saving Article")
print("-" * 30)

# TASK 9.1: Create article content (a string with multiple lines)
# This simulates a generated article from AI_SEO_Writer
article_content = """# Shilajit Benefits for Men

Shilajit is a powerful natural supplement that offers numerous health benefits.

## Key Benefits:
1. Increased energy levels
2. Improved testosterone
3. Better cognitive function

## Conclusion:
Shilajit is an excellent supplement for men's health.
"""

# TASK 9.2: Save the article to "shilajit_article.md" using with statement
with open("shilajit_article.md", "w") as file:
    file.write(article_content)

print("✅ Article saved to shilajit_article.md")

# TASK 9.3: Read the article back and print the first 100 characters
with open("shilajit_article.md", "r") as file:
    content = file.read()
    print("First 100 characters:")
    print(content[:100])

print()

# ============================================================
# SECTION 10: Real-World Scenario - Reading Competitor Articles
# ============================================================
print("SECTION 10: Real-World Scenario - Reading Competitor Articles")
print("-" * 30)

# TASK 10.1: Create a competitor article file first
competitor_content = """Competitor Article About Shilajit

This is a sample competitor article.
It contains information about shilajit benefits.
Word count: approximately 1500 words.
"""
with open("competitor_article.txt", "w") as file:
    file.write(competitor_content)

# TASK 10.2: Read the competitor article
with open("competitor_article.txt", "r") as file:
    competitor_text = file.read()

# TASK 10.3: Print the length of the article (number of characters)
article_length = len(competitor_text)
print(f"Competitor article length: {article_length} characters")

# TASK 10.4: Print the article content
print("Competitor article content:")
print(competitor_text)

print()

# ============================================================
# SECTION 11: Comparing Manual vs With Statement
# ============================================================
print("SECTION 11: Comparing Manual vs With Statement")
print("-" * 30)

# TASK 11.1: Write "Manual mode" using manual open/close
file_manual = open("comparison_manual.txt", "w")
file_manual.write("Manual mode")
file_manual.close()

# TASK 11.2: Write "With statement" using with statement
with open("comparison_with.txt", "w") as file:
    file.write("With statement")

# TASK 11.3: Read both files and print their contents
file_manual = open("comparison_manual.txt", "r")
manual_content = file_manual.read()
file_manual.close()

with open("comparison_with.txt", "r") as file:
    with_content = file.read()

print(f"Manual mode result: {manual_content}")
print(f"With statement result: {with_content}")
print("✅ Both methods work, but 'with' is recommended!")

print()

# ============================================================
# SECTION 12: File I/O + Lists (Combining Previous Concepts)
# ============================================================
print("SECTION 12: File I/O + Lists")
print("-" * 30)

# TASK 12.1: Create a list of 5 article titles
article_titles = ["Shilajit Benefits", "Shilajit Dosage", "Shilajit Side Effects", "Shilajit for Men", "Shilajit Reviews"]

# TASK 12.2: Write each title to "article_titles.txt" (one per line)
# Use a for loop to iterate through the list
with open("article_titles.txt", "w") as file:
    for title in article_titles:
        file.write(title + "\n")

print("✅ Article titles written to file")

# TASK 12.3: Read the file back and store lines in a list
with open("article_titles.txt", "r") as file:
    lines = file.readlines()

# TASK 12.4: Print the list length using len()
print(f"Number of articles: {len(lines)}")

# TASK 12.5: Print each title with its index (0, 1, 2, etc.)
for index, line in enumerate(lines):
    print(f"Article {index}: {line.strip()}")

print()

# ============================================================
# SECTION 13: File I/O + Functions (Combining Previous Concepts)
# ============================================================
print("SECTION 13: File I/O + Functions")
print("-" * 30)

# TASK 13.1: Define a function called 'save_to_file' that takes two parameters:
#   - filename (string)
#   - content (string)
# Inside, write the content to the file using with statement
def save_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

# TASK 13.2: Define a function called 'read_from_file' that takes one parameter:
#   - filename (string)
# Inside, read the file and return the content
def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()

# TASK 13.3: Call save_to_file with "function_test.txt" and "Hello from function!"
save_to_file("function_test.txt", "Hello from function!")

# TASK 13.4: Call read_from_file with "function_test.txt" and print the result
content = read_from_file("function_test.txt")
print(f"Content read by function: {content}")

print()

# ============================================================
# SECTION 14: File I/O + Loops (Combining Previous Concepts)
# ============================================================
print("SECTION 14: File I/O + Loops")
print("-" * 30)

# TASK 14.1: Create a list of 3 competitor URLs
competitor_urls = ["competitor1.com/shilajit", "competitor2.com/shilajit", "competitor3.com/shilajit"]

# TASK 14.2: Write each URL to "competitor_urls.txt" using a for loop
# Each URL should be on a new line
with open("competitor_urls.txt", "w") as file:
    for url in competitor_urls:
        file.write(url + "\n")

print("✅ Competitor URLs written")

# TASK 14.3: Read the file and process each URL with a loop
# Print each URL with a number (1, 2, 3, etc.)
with open("competitor_urls.txt", "r") as file:
    urls = file.readlines()
    for number, url in enumerate(urls, start=1):
        print(f"Competitor {number}: {url.strip()}")

print()

# ============================================================
# SECTION 15: File I/O + Control Flow (if/else) (Combining Previous Concepts)
# ============================================================
print("SECTION 15: File I/O + Control Flow")
print("-" * 30)

# TASK 15.1: Write "Important content" to "check_file.txt"
with open("check_file.txt", "w") as file:
    file.write("Important content\n")

# TASK 15.2: Read the file and check if content length is greater than 10
# If yes, print "File has enough content"
# If no, print "File is too short"
with open("check_file.txt", "r") as file:
    content = file.read()
    if len(content) > 10:
        print("File has enough content")
    else:
        print("File is too short")

# TASK 15.3: Read "check_file.txt" and check if it contains the word "Important"
# If yes, print "Found important content"
# If no, print "No important content found"
with open("check_file.txt", "r") as file:
    content = file.read()
    if "Important" in content:
        print("Found important content")
    else:
        print("No important content found")

print()

# ============================================================
# SECTION 16: File I/O + Dictionaries (Combining Previous Concepts)
# ============================================================
print("SECTION 16: File I/O + Dictionaries")
print("-" * 30)

# TASK 16.1: Create a dictionary with article information
# Keys: "title", "word_count", "status"
# Values: "Shilajit Guide", 2000, "published"
article_info = {
    "title": "Shilajit Guide",
    "word_count": 2000,
    "status": "published"
}

# TASK 16.2: Write each key-value pair to "article_info.txt"
# Format: "key: value" (one per line)
# Use a for loop to iterate through dictionary items
with open("article_info.txt", "w") as file:
    for key, value in article_info.items():
        file.write(f"{key}: {value}\n")

print("✅ Article info written to file")

# TASK 16.3: Read the file and recreate the dictionary
# Read each line, split by ":", and add to new dictionary
new_article_info = {}
with open("article_info.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        # Split line by ":" to get key and value
        parts = line.strip().split(": ")
        key = parts[0]
        value = parts[1]
        # Convert word_count to integer if it's a number
        if key == "word_count":
            value = int(value)
        new_article_info[key] = value

# TASK 16.4: Print the recreated dictionary
print(f"Recreated dictionary: {new_article_info}")

# TASK 16.5: Print just the title from the dictionary
print(f"Title: {new_article_info['title']}")

print()

# ============================================================
# SECTION 17: Challenge Problems (Combining Everything)
# ============================================================
print("SECTION 17: Challenge Problems (Combining Everything)")
print("-" * 30)

# CHALLENGE 17.1: Create a file called "challenge1.txt"
# Write 5 lines, each containing a number from 1 to 5
with open("challenge1.txt", "w") as file:
    for i in range(1, 6):
        file.write(f"Line {i}\n")

print("✅ Challenge 1: Created file with 5 numbered lines")

# CHALLENGE 17.2: Read "challenge1.txt" line by line using readlines()
# Print each line with its line number (1, 2, 3, etc.)
with open("challenge1.txt", "r") as file:
    lines = file.readlines()
    for index, line in enumerate(lines, start=1):
        print(f"Line {index}: {line.strip()}")

print()

# CHALLENGE 17.3: Create a file called "shopping_list.txt"
# Write 3 items: "Milk", "Bread", "Eggs" (each on a new line)
shopping_items = ["Milk\n", "Bread\n", "Eggs\n"]
with open("shopping_list.txt", "w") as file:
    file.writelines(shopping_items)

print("✅ Challenge 3: Created shopping list")

# CHALLENGE 17.4: Read "shopping_list.txt" and print each item
with open("shopping_list.txt", "r") as file:
    items = file.readlines()
    print("Shopping list items:")
    for item in items:
        print(f"  - {item.strip()}")

print()

# CHALLENGE 17.5: Append "Butter" to "shopping_list.txt"
with open("shopping_list.txt", "a") as file:
    file.write("Butter\n")

# Read and print the updated list
with open("shopping_list.txt", "r") as file:
    items = file.readlines()
    print("Updated shopping list:")
    for item in items:
        print(f"  - {item.strip()}")

print()

print("=" * 50)
print("FILE I/O PRACTICE COMPLETE!")
print("=" * 50)
print()
print("🎉 Great job! You've practiced:")
print("✅ Writing files (manual mode)")
print("✅ Reading files (manual mode)")
print("✅ Writing files (with statement)")
print("✅ Reading files (with statement)")
print("✅ Writing multiple lines")
print("✅ Reading line by line (readlines)")
print("✅ Writing multiple lines (writelines)")
print("✅ Append mode")
print("✅ Real-world scenarios")
print("✅ File I/O + Lists (combining concepts)")
print("✅ File I/O + Functions (combining concepts)")
print("✅ File I/O + Loops (combining concepts)")
print("✅ File I/O + Control Flow (combining concepts)")
print("✅ File I/O + Dictionaries (combining concepts)")
print("✅ Challenge problems")
print()
print("📚 Key Concepts Learned:")
print("  - open() with modes: 'r' (read), 'w' (write), 'a' (append)")
print("  - file.read() - reads all content")
print("  - file.write() - writes text")
print("  - file.readlines() - reads as list of lines")
print("  - file.writelines() - writes list of lines")
print("  - with statement - automatic file cleanup")
print("  - Manual mode - must remember to close()")
print()
print("Next: Error Handling (try/except) for files")
