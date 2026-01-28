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
file  = open("manual_write.txt", "w")

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
print(content)
print()

# ============================================================
# SECTION 3: Writing Files - With Statement (Recommended)
# ============================================================
print("SECTION 3: Writing Files - With Statement")
print("-" * 30)

# TASK 3.1: Write "Hello from with statement!" to "with_write.txt" using with statement
with open("with_write.txt", "w") as file_3:
    file_3.write("Hello from with statement!")

print("✅ File written using with statement (automatic close)")

print()

# ============================================================
# SECTION 4: Reading Files - With Statement (Recommended)
# ============================================================
print("SECTION 4: Reading Files - With Statement")
print("-" * 30)

# TASK 4.1: Read "with_write.txt" using with statement
with open("with_write.txt", "r") as file_4:
    content_4 = file_4.read()

# TASK 4.2: Print the content
print(content_4)
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
with open("multi_line.txt", "w") as file_5:
    file_5.write('Line 1: "First line"\n')
    file_5.write('Line 2: "Second line"\n')
    file_5.write('Line 3: "Third line"\n')

print("✅ Multiple lines written")

# TASK 5.2: Read and print the entire file
with open("multi_line.txt", "r") as file_5:
    content_5 = file_5.read()

print(content_5)
print()

# ============================================================
# SECTION 6: Reading Line by Line - readlines()
# ============================================================
print("SECTION 6: Reading Line by Line (readlines)")
print("-" * 30)

# TASK 6.1: Read "multi_line.txt" using readlines()
# This returns a LIST of lines (each line is a string)
with open("multi_line.txt", "r") as file_6:
    content_6 = file_6.readlines()

# TASK 6.2: Print the lines list (you'll see it's a list)
print(content_6)

# TASK 6.3: Print each line individually using a loop
for line in content_6:
    print(line)
print()

# ============================================================
# SECTION 7: Writing Multiple Lines - writelines()
# ============================================================
print("SECTION 7: Writing Multiple Lines (writelines)")
print("-" * 30)

# TASK 7.1: Create a list of strings (each string is a line)
# IMPORTANT: Each string must include "\n" at the end for proper line breaks
# Create 3 lines with text of your choice
list_string = ["line_1\n", "line_2\n", "line_3\n", "line_4\n"]

# TASK 7.2: Write all lines at once to "writelines_test.txt" using writelines()
# Use with statement and file.writelines(your_list)
with open("writelines_test.txt", "w") as new_file_7:
    new_file_7.writelines(list_string)

print("✅ Multiple lines written using writelines()")

# TASK 7.3: Read "writelines_test.txt" and print the file to verify
with open("writelines_test.txt", "r") as file_read_7:
    content_7 = file_read_7.read()
print(content_7)

print()

# ============================================================
# SECTION 8: Append Mode - Adding to Existing Files
# ============================================================
print("SECTION 8: Append Mode (Adding to Files)")
print("-" * 30)

# TASK 8.1: Write "Original content\n" to "append_test.txt" in write mode ("w")
# Use with statement
with open("append_test.txt", "w") as file_8:
    file_8.write("Original content\n")
# TASK 8.2: Append "New content\n" to "append_test.txt" using append mode ("a")
# Mode "a" = append (adds to end, doesn't overwrite existing content)
# Use with statement
with open("append_test.txt", "a") as file_8:
    file_8.write("New content\n")
# TASK 8.3: Read "append_test.txt" and print the entire file
# You should see both "Original content" and "New content"
with open("append_test.txt", "r") as file_8:
    content_8 = file_8.read()

print(content_8)
print()

# ============================================================
# SECTION 9: Real-World Scenario - Saving Article
# ============================================================
print("SECTION 9: Real-World Scenario - Saving Article")
print("-" * 30)

# TASK 9.1: Create article content (a string with multiple lines)
# Create a variable called 'article' with at least 3 lines about Shilajit
# Use "\n" to separate lines in the string
article = """
this is one line. this is another line. all these lines talk about shilajit. these lines are a part of the shilajit article. we will be using this article for testing file reading capabilities.
"""

# TASK 9.2: Save the article to "shilajit_article.md" using with statement
# Use write mode ("w")
with open("shilajit_article.md", "w") as file_9:
    file_9.write(article)

print("✅ Article saved to shilajit_article.md")

# TASK 9.3: Read "shilajit_article.md" back and print the first 100 characters
# Use string slicing: content[:100] to get first 100 characters
with open("shilajit_article.md", "r") as file_9:
    content = file_9.read()

print(content[:100])

print()

# ============================================================
# SECTION 10: Real-World Scenario - Reading Competitor Articles
# ============================================================
print("SECTION 10: Real-World Scenario - Reading Competitor Articles")
print("-" * 30)

# TASK 10.1: Create a competitor article file called "competitor_article.txt" first
# Write at least 2-3 lines of content about a health topic
# Use with statement and write mode
competiter_article = """This is a sample article about health. This article is written by our competiter. This article will be used to check our coding knowledge. 
"""
with open("competitor_article.txt", "w") as file_10:
    file_10.write(competiter_article)

# TASK 10.2: Read "competitor_article.txt" using with statement
# Store the content in a variable
with open("competitor_article.txt", "r") as file_10:
    content_10 = file_10.read()

# TASK 10.3: Print the length of the article (number of characters)
# Use len() function on the content variable
print(len(content_10))
# TASK 10.4: Print the article content
print(content_10)
print()

# ============================================================
# SECTION 11: Comparing Manual vs With Statement
# ============================================================
print("SECTION 11: Comparing Manual vs With Statement")
print("-" * 30)

# TASK 11.1: Write "Manual mode\n" to "manual_comparison.txt" using manual open/close
# Use open(), write(), close()
file_context = open("manual_comparison.txt", "w")
file_context.write("Manual mode\n")
file_context.close()

# TASK 11.2: Write "With statement\n" to "with_comparison.txt" using with statement
with open("with_comparison.txt", "w") as file_context:
    file_context.write("With statement\n")

# TASK 11.3: Read both files ("manual_comparison.txt" and "with_comparison.txt") and print their contents
file_content = open("manual_comparison.txt", "r")
print(file_content.read())

with open("with_comparison.txt", "r") as file_context:
    file_content = file_context.read()

print(file_content)

print("✅ Both methods work, but 'with' is recommended!")

print()

# ============================================================
# SECTION 12: File I/O + Lists (Combining Previous Concepts)
# ============================================================
print("SECTION 12: File I/O + Lists")
print("-" * 30)

# TASK 12.1: Create a list of 5 article titles
article_titles = ["title_1\n", "title_2\n", "title_3\n", "title_4\n", "title_5\n"]

# TASK 12.2: Write each title to "article_titles.txt" (one per line)
# Use a for loop to iterate through the list
with open("article_titles.txt", "w") as file_12:
    for title in article_titles:
        file_12.write(title)

print("✅ Article titles written to file")

# TASK 12.3: Read the file back and store lines in a list
with open("article_titles.txt", "r") as file_12:
    new_list = file_12.readlines()

# TASK 12.4: Print the list length using len()
print(len(new_list))

# TASK 12.5: Print each title with its index (0, 1, 2, etc.)
# Use enumerate() function: for index, title in enumerate(titles):
for index, title in enumerate(new_list):
    print(f"{index}: {title}")

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
        content_file = file.read()
    return content_file    

# TASK 13.3: Call save_to_file with "function_test.txt" and "Hello from function!"
save_to_file("function_test.txt", "Hello from function!")
# TASK 13.4: Call read_from_file with "function_test.txt" and print the result
print(read_from_file("function_test.txt"))
print()

# ============================================================
# SECTION 14: File I/O + Loops (Combining Previous Concepts)
# ============================================================
print("SECTION 14: File I/O + Loops")
print("-" * 30)

# TASK 14.1: Create a list of 3 competitor URLs
list_comp = ["url1.com", "url2.com", "url3.com"]
# TASK 14.2: Write each URL to "competitor_urls.txt" using a for loop
# Each URL should be on a new line
with open("competitor_urls.txt", "w") as new_file:
    for url in list_comp:
        new_file.write(url)
        new_file.write("\n")

print("✅ Competitor URLs written")

# TASK 14.3: Read "competitor_urls.txt" and process each URL with a loop
# Use readlines() to get a list of lines
# Print each URL with a number (1, 2, 3, etc.) using enumerate() with start=1
with open("competitor_urls.txt", "r") as file_14:
    list = file_14.readlines()
for index, item in enumerate(list):
    print(f"{index}: {item}")

print()

# ============================================================
# SECTION 15: File I/O + Control Flow (if/else) (Combining Previous Concepts)
# ============================================================
print("SECTION 15: File I/O + Control Flow")
print("-" * 30)

# TASK 15.1: Write "Important content" to "check_file.txt"
with open("check_file.txt", "w") as file:
    file.write("Important content")
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
article_information = {
    "title": "Shilajit Guide",
    "word_count": 2000,
    "status": "published"
}

# TASK 16.2: Write each key-value pair to "article_info.txt"
# Format: "key: value" (one per line)
# Use a for loop to iterate through dictionary items
with open("article_info.txt", "w") as file:
    for key, value in article_information.items():
        file.write(f"{key}: {value}")
        file.write("\n")

print("✅ Article info written to file")

# TASK 16.3: Read "article_info.txt" and recreate the dictionary
# Use readlines() to get list of lines
# For each line, use split(": ") to separate key and value
# Create a new empty dictionary and add each key-value pair

# TASK 16.4: Print the recreated dictionary


# TASK 16.5: Print just the title from the dictionary

print()

# ============================================================
# SECTION 17: Challenge Problems (Combining Everything)
# ============================================================
print("SECTION 17: Challenge Problems (Combining Everything)")
print("-" * 30)

# CHALLENGE 17.1: Create a file called "challenge1.txt"
# Write 5 lines, each containing a number from 1 to 5

print("✅ Challenge 1: Created file with 5 numbered lines")

# CHALLENGE 17.2: Read "challenge1.txt" line by line using readlines()
# Print each line with its line number (1, 2, 3, etc.)
# Use enumerate() with start=1 to number the lines

print()

# CHALLENGE 17.3: Create a file called "shopping_list.txt"
# Write 3 items: "Milk", "Bread", "Eggs" (each on a new line)

print("✅ Challenge 3: Created shopping list")

# CHALLENGE 17.4: Read "shopping_list.txt" and print each item

print()

# CHALLENGE 17.5: Append "Butter\n" to "shopping_list.txt" using append mode ("a")

# Read "shopping_list.txt" and print the updated list

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
