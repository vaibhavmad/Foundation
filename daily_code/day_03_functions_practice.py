"""
Foundation Day 3 - Functions Practice
Date: January 23, 2026
Goal: Understand and practice Python functions

Instructions:
- Read each section
- Write the code yourself (don't copy-paste from comments)
- Run the file to see results: python3 daily_code/day_03_functions_practice.py
- Experiment and break things to learn!
"""

print("=" * 50)
print("FOUNDATION DAY 3 - FUNCTIONS PRACTICE")
print("=" * 50)
print()

# ============================================================
# SECTION 1: Defining Simple Functions
# ============================================================
print("SECTION 1: Defining Simple Functions")
print("-" * 30)

# TASK 1.1: Define a function called 'greet' that prints "Hello!"
def greet():
    print("Hello!")

# TASK 1.2: Call the function (run it)
greet()

# TASK 1.3: Define a function called 'say_goodbye' that prints "Goodbye!"
def say_goodbye():
    print("Goodbye!")

# TASK 1.4: Call the say_goodbye function
say_goodbye()

print()

# ============================================================
# SECTION 2: Functions with Parameters
# ============================================================
print("SECTION 2: Functions with Parameters")
print("-" * 30)

# TASK 2.1: Define a function called 'greet_person' that takes one parameter called 'name'
# Inside the function, print: "Hello, [name]!"
def greet_person(name):
    print(f"Hello, {name}!")

# TASK 2.2: Call greet_person with the argument "Alice"
greet_person("Alice")

# TASK 2.3: Call greet_person with your own name
greet_person("My_Name")

print()

# ============================================================
# SECTION 3: Functions with Return Values
# ============================================================
print("SECTION 3: Functions with Return Values")
print("-" * 30)

# TASK 3.1: Define a function called 'add_numbers' that takes two parameters: 'a' and 'b'
# Inside the function, calculate a + b and RETURN the result
def add_numbers(a, b):
    return a + b

# TASK 3.2: Call add_numbers with arguments 5 and 3, store the result in a variable called 'sum'
sum = add_numbers(5, 3)

# TASK 3.3: Print the sum
print(sum)

# TASK 3.4: Call add_numbers with 10 and 20, print the result directly
print(add_numbers(10, 20))

print()

# ============================================================
# SECTION 4: Calling Functions Multiple Times
# ============================================================
print("SECTION 4: Calling Functions Multiple Times")
print("-" * 30)

# TASK 4.1: Define a function called 'multiply' that takes two parameters and returns their product
def multiply(x, y):
    return x * y

# TASK 4.2: Call multiply three times with different numbers, print each result
print(multiply(2, 3))
print(multiply(3, 4))
print(multiply(4, 5))

print()

# ============================================================
# SECTION 5: Functions Calling Other Functions
# ============================================================
print("SECTION 5: Functions Calling Other Functions")
print("-" * 30)

# TASK 5.1: Define a function called 'get_word_count' that takes one parameter 'url'
# Inside, create a dictionary with 3 URLs as keys and word counts as values
# Check if the url exists in the dictionary
# If it exists, return the word count
# If not, return 0
def get_word_count(url):
    new_dict = {
        "comp1.com/article": 1200,
        "comp2.com/article": 2200,
        "comp3.com/article": 3200
    }
    if url in new_dict:
        return new_dict[url]
    else:
        return 0

# TASK 5.2: Define a function called 'analyze_url' that takes one parameter 'url'
# Inside, call get_word_count(url) and store the result
# If the word count is greater than 1700, return "Long article"
# Otherwise, return "Short article"
def analyze_url(url):
    word_check = get_word_count(url)
    if word_check > 1700:
        return "Long Article"
    else:
        return "Short Article"

# TASK 5.3: Call analyze_url with "comp1.com/article" and print the result
print(analyze_url("comp1.com/article"))

# TASK 5.4: Call analyze_url with "comp2.com/article" and print the result
print(analyze_url("comp2.com/article"))

print()

# ============================================================
# SECTION 6: Functions Returning Dictionaries
# ============================================================
print("SECTION 6: Functions Returning Dictionaries")
print("-" * 30)

# TASK 6.1: Define a function called 'get_article_info' that takes one parameter 'title'
# Inside, return a dictionary with:
#   - "title": the title parameter
#   - "word_count": 2000
#   - "status": "draft"
def get_article_info(title):
    return {
        "title": title,
        "word_count": 2000,
        "status": "draft"
    }

# TASK 6.2: Call get_article_info with "Shilajit Benefits" and store the result
shilajit_article_info = get_article_info("Shilajit Benefits")

# TASK 6.3: Print the entire dictionary
print(shilajit_article_info)

# TASK 6.4: Print just the title from the dictionary
print(shilajit_article_info["title"])

# TASK 6.5: Print just the word_count from the dictionary
print(shilajit_article_info["word_count"])

print()

# ============================================================
# SECTION 7: Functions with Lists as Parameters
# ============================================================
print("SECTION 7: Functions with Lists as Parameters")
print("-" * 30)

# TASK 7.1: Define a function called 'count_items' that takes one parameter 'items' (a list)
# Inside, return the length of the list using len()
def count_items(items):
    return len(items)

# TASK 7.2: Create a list with 3 items: ["apple", "banana", "orange"]
new_list = [
    "apple",
    "banana",
    "orange"
]

# TASK 7.3: Call count_items with your list and print the result
print(count_items(new_list))

# TASK 7.4: Define a function called 'sum_numbers' that takes one parameter 'numbers' (a list)
# Inside, loop through the list and add up all the numbers
# Return the total
def sum_numbers(numbers):
    total_num = 0
    for i in numbers:
        total_num += i
    return total_num

# TASK 7.5: Create a list of numbers: [10, 20, 30, 40]
numbers = [10, 20, 30, 40]

# TASK 7.6: Call sum_numbers with your list and print the result
print(sum_numbers(numbers))

print()

# ============================================================
# SECTION 8: Real-World Scenario (AI_SEO_Writer)
# ============================================================
print("SECTION 8: Real-World Scenario")
print("-" * 30)

# TASK 8.1: Define a function called 'check_article_length' that takes one parameter 'word_count'
# If word_count is greater than or equal to 2000, return "Good length"
# Otherwise, return "Too short"
def check_article_length(word_count):
    if word_count >= 2000:
        return "Good Length"
    else:
        return "Too Short"

# TASK 8.2: Call check_article_length with 2500 and print the result
print(check_article_length(2500))

# TASK 8.3: Call check_article_length with 1500 and print the result
print(check_article_length(1500))

# TASK 8.4: Define a function called 'analyze_competitors' that takes one parameter 'urls' (a list)
# Inside, loop through each URL
# For each URL, call get_word_count(url) from Section 5
# Add up all the word counts
# Calculate the average (total / number of URLs)
# Return a dictionary with:
#   - "total_competitors": number of URLs
#   - "total_words": sum of all word counts
#   - "avg_word_count": average word count
def analyze_competitors(urls):
    total_words = 0
    total_competitors = 0
    for i in urls:
        total_words += get_word_count(i)
        total_competitors += 1
    avg_word_count = total_words / total_competitors
    return {
        "total_competitors": total_competitors,
        "total_words": total_words,
        "avg_word_count": avg_word_count
    }

# TASK 8.5: Create a list of 3 competitor URLs
urls_list_new = [
    "comp1.com/article",
    "comp2.com/article",
    "comp3.com/article"
]

# TASK 8.6: Call analyze_competitors with your list and store the result
result_analysis = analyze_competitors(urls_list_new)

# TASK 8.7: Print the entire result dictionary
print(result_analysis)

# TASK 8.8: Print just the average word count
print(result_analysis["avg_word_count"])

print()

# ============================================================
# SECTION 9: Challenge Problems
# ============================================================
print("SECTION 9: Challenge Problems")
print("-" * 30)

# CHALLENGE 9.1: Define a function called 'calculate_total' that takes a list of prices
# Return the sum of all prices
def calculate_total(list_of_prices):
    total_price = 0
    for price in list_of_prices:
        total_price += price
    return total_price

# CHALLENGE 9.2: Call calculate_total with [10.50, 20.75, 5.25] and print the result
price_list = [10.50, 20.75, 5.25]
print(calculate_total(price_list))

# CHALLENGE 9.3: Define a function called 'get_max_word_count' that takes a list of word counts
# Return the highest word count in the list
def get_max_word_count(list_of_word_counts):
    max_word_count = 0
    for word_counts in list_of_word_counts:
        if word_counts > max_word_count:
            max_word_count = word_counts
    return max_word_count
# CHALLENGE 9.4: Call get_max_word_count with [1500, 2000, 1800, 2200] and print the result
word_list_new = [1500, 2000, 1800, 2200]
print(get_max_word_count(word_list_new))

# CHALLENGE 9.5: Define a function called 'create_article_summary' that takes:
#   - title (string)
#   - word_count (number)
#   - status (string)
# Return a dictionary with all three values
def create_article_summary(title, word_count, status):
    return {
        "Title": title,
        "Word Count": word_count,
        "Status": status
    }

# CHALLENGE 9.6: Call create_article_summary and print the result
print(create_article_summary("This is Article Title", 2900, "Published"))

print()
print("=" * 50)
print("FUNCTIONS PRACTICE COMPLETE!")
print("=" * 50)
print()
print("🎉 Great job! You've practiced:")
print("✅ Defining functions")
print("✅ Functions with parameters")
print("✅ Functions with return values")
print("✅ Calling functions")
print("✅ Functions calling other functions")
print("✅ Functions returning dictionaries")
print("✅ Functions with lists as parameters")
print("✅ Real-world scenarios")
print()
print("🎊 Day 3 Functions COMPLETE!")
print("Next: Day 4 - Imports + Loops")
