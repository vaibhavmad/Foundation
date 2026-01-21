# Foundation Day 1 - Python Basics Knowledge Validation
# 
# INSTRUCTIONS:
# - Read each problem/question in the comments
# - Write your code/answer below each problem
# - Do NOT look up answers - test your current knowledge
# - If you don't know something, write "DON'T KNOW" and move on
# - Run the file after completing to check your answers work
#
# To run: python day_01_python_basics_quiz.py

print("=" * 60)
print("FOUNDATION DAY 1 - PYTHON BASICS QUIZ")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: VARIABLES & ASSIGNMENT (Easy)
# ============================================================================

print("SECTION 1: Variables & Assignment")
print("-" * 40)

# PROBLEM 1.1 (EASY):
# Create a variable called 'name' and assign your name to it (as a string)
# Then print it

# YOUR CODE HERE:
name = "sys_admin_vm"
print(name)


# PROBLEM 1.2 (EASY):
# Create a variable called 'age' and assign the number 38 to it
# Then print it

# YOUR CODE HERE:
age = 38
print(age)


# PROBLEM 1.3 (EASY):
# Create a variable called 'city' with value "Gurgaon"
# Create a variable called 'country' with value "India"
# Print both on the same line with a comma between them
# Expected output: Gurgaon, India

# YOUR CODE HERE:
city = "Gurgaon"
country = "India"
print(f"{city}, {country}") 



# ============================================================================
# SECTION 2: DATA TYPES (Easy to Medium)
# ============================================================================

print("\nSECTION 2: Data Types")
print("-" * 40)

# PROBLEM 2.1 (EASY):
# Create these variables:
# - product_name (string): "Shilajit"
# - price (float): 29.99
# - in_stock (boolean): True
# - quantity (integer): 150

# YOUR CODE HERE:
product_name = "Shilajit"
price = 29.99
in_stock = True
quantity = 150



# PROBLEM 2.2 (MEDIUM):
# What data type is each of these? Write as a comment next to each:
example_1 = "Hello"        # Data type: string
example_2 = 42             # Data type: int
example_3 = 3.14           # Data type: float
example_4 = True           # Data type: bool
example_5 = "123"          # Data type: string




# PROBLEM 2.3 (MEDIUM):
# Create a variable 'article_count' with value 11 (integer)
# Create a variable 'cost_per_article' with value 0.35 (float)
# Print both with descriptive text

# YOUR CODE HERE:
article_count = 11
cost_per_article = 0.35
print(f"Article Count is {article_count}")
print(f"Cost per article is {cost_per_article}")

# ============================================================================
# SECTION 3: BASIC OPERATORS (Easy to Medium)
# ============================================================================

print("\nSECTION 3: Basic Operators")
print("-" * 40)

# PROBLEM 3.1 (EASY):
# Calculate: 5 + 3 and store in a variable called 'sum_result'
# Print the result

# YOUR CODE HERE:
sum_result = 5 + 3
print(sum_result)



# PROBLEM 3.2 (EASY):
# Calculate: 10 - 4 and store in 'difference'
# Calculate: 6 * 7 and store in 'product'
# Calculate: 20 / 5 and store in 'quotient'
# Print all three

# YOUR CODE HERE:
difference = 10 - 4
product = 6 * 7
quotient = 20 / 5
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")

# PROBLEM 3.3 (MEDIUM):
# You have 100 articles to generate
# Each article costs $0.45
# Calculate total cost and store in 'total_cost'
# Print: "Total cost for 100 articles: $XX.XX"

# YOUR CODE HERE:
article_count_total = 100
per_article_cost = 0.45 #dollars
total_cost_is = article_count_total * per_article_cost #variable names as different to avoid duplication 
print(f"Total cost for 100 articles: ${total_cost_is}")

# PROBLEM 3.4 (MEDIUM):
# Create variable 'budget' with value 50.0 (float)
# Create variable 'cost_per_article' with value 0.45 (float)
# Calculate how many articles you can afford (division)
# Store in 'articles_possible'
# Print the result

# YOUR CODE HERE:
budget = 50.0
cost_per_article = 0.45
you_can_afford = budget // cost_per_article
print(f"You can afford {you_can_afford} articles.")


# ============================================================================
# SECTION 4: print() FUNCTION (Easy to Medium)
# ============================================================================

print("\nSECTION 4: print() Function")
print("-" * 40)

# PROBLEM 4.1 (EASY):
# Print the text: Hello, Foundation Day 1!

# YOUR CODE HERE:
print("Hello, Foundation Day 1!")


# PROBLEM 4.2 (EASY):
# Create a variable 'project_name' with value "AI_SEO_Writer"
# Print: Working on: AI_SEO_Writer

# YOUR CODE HERE:
project_name = "AI_SEO_Writer"
print(f"Working on: {project_name}")


# PROBLEM 4.3 (MEDIUM):
# Print multiple values in one print statement:
# Variable 'name' (create it with your name)
# Text "is learning Python on"
# Variable 'date' (create it with "January 21, 2026")
# Expected output: nmcpharma is learning Python on January 21, 2026

# YOUR CODE HERE:
name = "sys_admin_vm"
text = "is learning Python on"
date = "January 21, 2026"
print(f"{name} {text} {date}")
# Expected output: nmcpharma is learning Python on January 21, 2026


# PROBLEM 4.4 (MEDIUM):
# Create variables: articles = 5, cost = 0.35
# Print them together with descriptive text
# Expected output: Generated 5 articles at $0.35 each

# YOUR CODE HERE:
articles, cost = 5, 0.35
print(f"Generated {articles} at ${cost} each")



# ============================================================================
# SECTION 5: COMMENTS (Easy)
# ============================================================================

print("\nSECTION 5: Comments")
print("-" * 40)

# PROBLEM 5.1 (EASY):
# Add a single-line comment above this variable explaining what it represents
# (Write the comment, then uncomment the variable line below)

# Test api key
api_key = "sk-test12345"



# PROBLEM 5.2 (EASY):
# Add comments explaining each line of this code:

# variable website with value of dailyveda.in
website = "dailyveda.in"

# variable active_users with value of 405 assigned to it 
active_users = 405

# variable avg_session_time with value of 3.5 assigned to it
avg_session_time = 3.5




# ============================================================================
# SECTION 6: MIXED PROBLEMS (Medium to Hard)
# ============================================================================

print("\nSECTION 6: Mixed Problems")
print("-" * 40)

# PROBLEM 6.1 (MEDIUM):
# You're tracking OpenAI API costs.
# Create these variables:
# - api_calls_today: 25 (integer)
# - cost_per_call: 0.05 (float)
# Calculate total cost and print: "Today's API cost: $X.XX"

# YOUR CODE HERE:
api_calls_today = 25
cost_per_call = 0.05
total_api_cost = api_calls_today * cost_per_call
print(f"Today's API cost: ${total_api_cost}")




# PROBLEM 6.2 (MEDIUM):
# Create variables for a blog article:
# - title: "Shilajit Benefits for Men Over 40" (string)
# - word_count: 1987 (integer)
# - generation_cost: 0.23 (float)
# - published: False (boolean)
# Print all four with descriptive labels

# YOUR CODE HERE:
title = "Shilajit Benefits for Men Over 40"
word_count = 1987
generation_cost = 0.23
published = False

print(f"Article title is: {title}")
print(f"Word count is: {word_count}")
print(f"Total generation cost is ${generation_cost}")
print(f"Is it published yet: {published}")



# PROBLEM 6.3 (HARD):
# DailyVeda.in statistics:
# - You have 11 articles currently
# - Each article gets 37 visitors per day on average
# - You want to reach 1000 visitors per day
# Calculate:
#   a) Current daily visitors (11 * 37)
#   b) How many more visitors you need (1000 - current)
#   c) How many more articles needed (divide visitors_needed by 37)
# Print all three results with clear labels

# YOUR CODE HERE:
total_articles = 11
daily_per_article_visits = 37
current_daily_visits = total_articles * daily_per_article_visits
visitors_needed = 1000 - current_daily_visits
articles_needed = visitors_needed / daily_per_article_visits
print(f"Current daily visits are: {current_daily_visits}")
print(f"Visitors needed to reach 1000: {visitors_needed}")
print(f"Total articles needed: {articles_needed}")


# PROBLEM 6.4 (HARD):
# Cost optimization calculation:
# You generated 3 articles yesterday:
# - Article 1: 1847 words, cost $0.32
# - Article 2: 2103 words, cost $0.41  
# - Article 3: 1654 words, cost $0.28
# 
# Calculate:
# a) Total words written
# b) Total cost
# c) Average cost per article
# d) Average cost per 1000 words
# Print all results with 2 decimal places

# YOUR CODE HERE:
words_article_1 = 1847
words_article_2 = 2103
words_article_3 = 1654

cost_article_1 = 0.32
cost_article_2 = 0.41
cost_article_3 = 0.28

total_words_written = words_article_1 + words_article_2 + words_article_3

total_cost = cost_article_1 + cost_article_2 + cost_article_3
average_cost = total_cost / 3

total_1000_words_units = total_words_written / 1000
average_cost_1000_words = total_cost/total_1000_words_units

print(f"Total words written: {total_words_written}")
print(f"Total cost: ${total_cost}")
print(f"Average cost per article: ${average_cost}")
print(f"Average cost per 1000 words: ${average_cost_1000_words}")


# ============================================================================
# SECTION 7: CONCEPTUAL QUESTIONS (Write answers as comments)
# ============================================================================

print("\nSECTION 7: Conceptual Questions")
print("-" * 40)

# QUESTION 7.1:
# What's the difference between 42 and "42"?
# YOUR ANSWER (as comment):
# 42 is int, "42" is a string



# QUESTION 7.2:
# Why use variables instead of just writing values directly?
# YOUR ANSWER (as comment):
# so that you can use that value at multiple places and incase value needs
# to be edited, you can simply change the value of variable, it will change 
# the value across program



# QUESTION 7.3:
# What happens if you try to do: 5 + "3"
# (Don't test it, just answer what you think will happen)
# YOUR ANSWER (as comment):
# it will most probably give type error, since you 
# can not add int to strings



# QUESTION 7.4:
# In this code: api_key = os.getenv("OPENAI_API_KEY")
# What data type is 'api_key'? (Hint: what does getenv return?)
# YOUR ANSWER (as comment):
# since OPEN_API_KEY is enclosed in "", hence i beleive it is string



# ============================================================================
# BONUS CHALLENGE (Optional - Hard)
# ============================================================================

print("\nBONUS CHALLENGE")
print("-" * 40)

# CHALLENGE:
# AI_SEO_Writer cost projection:
# - You want to generate 100 articles per month for dailyveda.in
# - OpenAI costs $0.45 per article on average
# - You have a monthly budget of $50
# 
# Questions:
# a) Can you afford 100 articles per month? (True/False)
# b) What's the total cost for 100 articles?
# c) If budget is $50, how many articles can you afford?
# d) How much would you need to save per day to afford 100 articles in 30 days?
#
# Calculate all four and print with clear labels

# YOUR CODE HERE:
# a. for this, we need to check the total count of articles we can 
# write using our budget
monthly_budget = 50
cost_per_article_budget = 0.45
total_articles_possible = monthly_budget / cost_per_article_budget

affordability = False
if total_articles_possible >= 100:
    affordability = True

total_cost_100_articles = 100 * cost_per_article_budget

print(f"a) Can you afford 100 articles per month?: {affordability}")
print(f"b) What's the total cost for 100 articles?: ${total_cost_100_articles}")
print(f"Total articles possible: {total_articles_possible}")

total_days = 30
savings_per_day = total_cost_100_articles / total_days
print(f"# d) How much would you need to save per day to afford 100 articles in 30 days?: ${savings_per_day}")


# ============================================================================
print("\n" + "=" * 60)
print("QUIZ COMPLETE!")
print("=" * 60)
print("\nSave this file and tell me when you're done.")
print("I'll review your answers and identify any gaps.")
print("\nTo run and check: python day_01_python_basics_quiz.py")
