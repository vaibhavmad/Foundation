"""
Day 3: Functions = Simple Examples
Focus: Function definition, calling parameters and triple
quotes
"""

urls = {
    "comp1.com/topic": 2300,
    "comp2.com/topic": 2400,
    "comp3.com/topic": 2500,
    "comp4.com/topic": 2600,
    "comp5.com/topic": 2700,
}

def get_word_count(url):
    if url in urls:
        word_count = (urls[url])
        return word_count
    else:
        return 0

result1 = get_word_count("comp1.com/topic")

result2 = get_word_count("unknown.com")


url_list = [
    "comp1.com/topic",
    "comp2.com/topic",
    "comp3.com/topic",
    "comp4.com/topic",
    "comp5.com/topic",
]

def analyze_competitors(competitor_urls):
    word_count = 0
    comp_count = 0
    for i in competitor_urls:
        print(i)
        word_count += get_word_count(i)
        comp_count += 1
    avg_words = word_count / comp_count
    return {
        "total_competitors": comp_count,
        "total_words": word_count,
        "avg_word_count": avg_words
    }
print(analyze_competitors(url_list))

