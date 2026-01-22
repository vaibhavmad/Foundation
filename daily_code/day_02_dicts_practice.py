"""
Foundation Day 2 - Dictionaries Practice
Date: January 21, 2026
Goal: Understand and practice Python dictionaries (key-value pairs)

Instructions:
- Read each section
- Write the code yourself
- Run the file to see results: python3 daily_code/day_02_dicts_practice.py
- Experiment and break things to learn!
"""

# from nt import remove


print("=" * 50)
print("FOUNDATION DAY 2 - DICTIONARIES PRACTICE")
print("=" * 50)
print()

# ============================================================
# SECTION 1: Creating Dictionaries
# ============================================================
print("SECTION 1: Creating Dictionaries")
print("-" * 30)

# TASK 1.1: Create an empty dictionary called 'my_dict'
my_dict = {}

# TASK 1.2: Create a dictionary for an article with these key-value pairs:
# - "title": "Shilajit Benefits"
# - "word_count": 2000
# - "status": "draft"
# Call it 'article'
article = {
    "title": "Shilajit Benefits", 
    "word_count": 2000,
    "status": "draft"
}

# TASK 1.3: Create a dictionary for a project with:
# - "name": "AI SEO Writer"
# - "language": "Python"
# - "days_spent": 2
# Call it 'project'
project = {
    "name": "AI SEO Writer",
    "language": "Python",
    "days_spent": 2
}

# TASK 1.4: Print all three dictionaries
print(my_dict)
print(article)
print(project)


print()

# ============================================================
# SECTION 2: Accessing Values by Key
# ============================================================
print("SECTION 2: Accessing Values by Key")
print("-" * 30)

competitor = {
    "url": "https://competitor1.com/shilajit",
    "word_count": 1847,
    "ranking": 3,
    "has_images": True
}

# TASK 2.1: Print the URL
print(competitor["url"])

# TASK 2.2: Print the word count
print(competitor["word_count"])

# TASK 2.3: Print the ranking
print(competitor["ranking"])

# TASK 2.4: Print whether it has images
print(competitor["has_images"])

# TASK 2.5: What happens if you try a key that doesn't exist? (Uncomment to test)
# print(competitor["author"])
# KeyError: 'author'

print()

# ============================================================
# SECTION 3: Modifying Dictionary Values
# ============================================================
print("SECTION 3: Modifying Dictionary Values")
print("-" * 30)

article_data = {
    "title": "Draft Title",
    "word_count": 0,
    "status": "not started"
}

# TASK 3.1: Print the original dictionary
print(f"Original dict: {article_data}")

# TASK 3.2: Change the title to "Shilajit Benefits for Men"
article_data["title"] = "Shilajit Benefits for Men"

# TASK 3.3: Change word_count to 2000
article_data["word_count"] = 2000

# TASK 3.4: Change status to "complete"
article_data["status"] = "complete"

# TASK 3.5: Print the modified dictionary
print("Modified:", article_data)

print()

# ============================================================
# SECTION 4: Adding New Key-Value Pairs
# ============================================================
print("SECTION 4: Adding New Key-Value Pairs")
print("-" * 30)

analysis = {
    "topic": "shilajit"
}
print("Starting dict:", analysis)

# TASK 4.1: Add "avg_word_count" with value 1800
analysis["avg_word_count"] = 1800

# TASK 4.2: Add "num_competitors" with value 5
analysis["num_competitors"] = 5

# TASK 4.3: Add "content_gap" with value "dosage for men 40+"
analysis["content_gap"] = "dosage for men 40+"

# TASK 4.4: Print the final dictionary
print("Final dict:", analysis)

print()

# ============================================================
# SECTION 5: Removing Key-Value Pairs
# ============================================================
print("SECTION 5: Removing Key-Value Pairs")
print("-" * 30)

api_response = {
    "title": "Article Title",
    "content": "Article content here...",
    "metadata": "internal use only",
    "temp_data": "delete this"
}
print("Original:", api_response)

# TASK 5.1: Remove "temp_data" key
del api_response["temp_data"]

# TASK 5.2: Remove "metadata" key
del api_response["metadata"]

# TASK 5.3: Print the cleaned dictionary
print("Cleaned:", api_response)

print()

# ============================================================
# SECTION 6: Dictionary Operations
# ============================================================
print("SECTION 6: Dictionary Operations")
print("-" * 30)

project_info = {
    "name": "AI SEO Writer",
    "status": "in progress",
    "days": 2,
    "completed": False
}

# TASK 6.1: Print how many key-value pairs are in the dictionary
# 4

# TASK 6.2: Check if "name" key exists in the dictionary
# Print "Name exists!" if it does
if "name" in project_info:
    print("Name exists!")
else:
    print("Name does not exist")

# TASK 6.3: Check if "author" key exists
# Print "Author exists!" if it does, otherwise print "Author not found"
if "author" in project_info:
    print("Author exists!")
else:
    print("Author does not exist")


# TASK 6.4: Get all the keys and print them
project_keys = project_info.keys()
print(f"Keys: {project_keys}")

# TASK 6.5: Get all the values and print them
project_values = project_info.values()
print(f"Values: {project_values}")

print()

# ============================================================
# SECTION 7: Nested Structures - List of Dictionaries
# ============================================================
print("SECTION 7: List of Dictionaries (Nested)")
print("-" * 30)

competitors = [
    {"name": "Competitor A", "word_count": 1500, "ranking": 5},
    {"name": "Competitor B", "word_count": 2000, "ranking": 3},
    {"name": "Competitor C", "word_count": 1800, "ranking": 4}
]

# TASK 7.1: Print the ENTIRE list
print(competitors)

# TASK 7.2: Print the FIRST competitor (it's a dictionary!)
print(competitors[0])

# TASK 7.3: Print the name of the FIRST competitor
print(competitors[0]["name"])

# TASK 7.4: Print the word_count of the SECOND competitor
print(competitors[1]["word_count"])

# TASK 7.5: Print the ranking of the THIRD competitor
print(competitors[2]["ranking"])

print()

# ============================================================
# SECTION 8: Real-World - OpenAI Message Format
# ============================================================
print("SECTION 8: Real-World - OpenAI Messages")
print("-" * 30)

# TASK 8.1: Create a messages list with ONE dictionary inside
# The dictionary should have:
# - "role": "user"
# - "content": "Generate a headline about shilajit benefits"
# Call it 'messages'
message = [
    {
        "role": "user",
        "content": "Generate a headline about shilajit benefits"
    }
]

# TASK 8.2: Print the entire messages list
print(message)

# TASK 8.3: Print JUST the first message (the dictionary)
print(message[0])

# TASK 8.4: Print JUST the role from the first message
print(message[0]["role"])

# TASK 8.5: Print JUST the content from the first message
print(message[0]["content"])

print()

# ============================================================
# SECTION 9: Dictionary Inside Dictionary (Advanced)
# ============================================================
print("SECTION 9: Nested Dictionaries")
print("-" * 30)

article_full = {
    "title": "Shilajit Benefits",
    "details": {
        "word_count": 2000,
        "keywords": ["shilajit", "benefits", "dosage"],
        "status": "draft"
    }
}

# TASK 9.1: Print the title
print(article_full["title"])

# TASK 9.2: Print the ENTIRE details dictionary
print(article_full["details"])

# TASK 9.3: Print the word_count from inside details
print(article_full["details"]["word_count"])

# TASK 9.4: Print the status from inside details
print(article_full["details"]["status"])

# TASK 9.5: Print the FIRST keyword from the keywords list inside details
article_keywords = article_full["details"]["keywords"]
print(article_keywords[0])

print()

# ============================================================
# SECTION 10: Challenge Problems
# ============================================================
print("SECTION 10: Challenge Problems")
print("-" * 30)

# CHALLENGE 10.1: Create a dictionary for a competitor with at least 4 keys
# Include: url, word_count, ranking, and one more of your choice
competitor_a = {
    "url": "xyz1.com",
    "word_count": 2100,
    "ranking": 4,
    "evaluated": False
}

# CHALLENGE 10.2: Create a list with 3 dictionaries
# Each dictionary should represent an article with "title" and "word_count"
article_info_list = [
    {
        "title": "Hello Code", 
        "word_count": 2100
    },
    {
        "title": "Hello Code1", 
        "word_count": 2200
    },
    {
        "title": "Hello Code2", 
        "word_count": 2300
    }
]

# CHALLENGE 10.3: From your list in 10.2, print the title of the SECOND article
print(article_info_list[1]["title"])

# CHALLENGE 10.4: Create a dictionary that contains:
# - "project": "Foundation"
# - "topics": a LIST of 3 topics you've learned
# - "progress": a DICTIONARY with "days": 2, "complete": False
learning_status = {
    "project": "Foundation",
    "topics": ["git", "variables", "operators"],
    "progress": {
        "days": 2,
        "complete": False
    }
}

# CHALLENGE 10.5: From 10.4, print how many days from the nested progress dictionary
print(learning_status["progress"]["days"])

print()
print("=" * 50)
print("DICTIONARIES PRACTICE COMPLETE!")
print("=" * 50)
print()
print("🎉 Great job! You've practiced:")
print("✅ Creating dictionaries")
print("✅ Accessing values by key")
print("✅ Modifying dictionaries")
print("✅ Adding and removing key-value pairs")
print("✅ Dictionary operations (len, in, keys, values)")
print("✅ List of dictionaries (nested)")
print("✅ OpenAI message format")
print("✅ Dictionary inside dictionary")
print()
print("🎊 Day 2 COMPLETE! Lists + Dictionaries mastered!")
print("Next: Git commit your Day 2 code")
