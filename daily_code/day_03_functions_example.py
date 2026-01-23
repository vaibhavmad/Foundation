"""
Day 3: Functions Example - Complete Data Example
Demonstrates analyze_competitors function with real data

FOCUS: Function definition, calling, parameters, and return values
"""

# ============================================================
# FUNCTION 1: get_word_count
# ============================================================

def get_word_count(url):
    mock_word_counts = {
        "https://competitor1.com/shilajit": 1850,
        "https://competitor2.com/shilajit": 2100,
        "https://competitor3.com/shilajit": 1750,
        "https://competitor4.com/shilajit": 1950,
        "https://competitor5.com/shilajit": 2000
    }
    if url in mock_word_counts:
        word_count = mock_word_counts[url]
        return word_count
    else:
        return 0



# ============================================================
# FUNCTION 2: analyze_competitors
# ============================================================
# This function takes a LIST of URLs and analyzes them all

def analyze_competitors(competitor_urls):
    total_words = 0
    for url in competitor_urls:
        word_count = get_word_count(url)
        total_words += word_count
        print(f"  Analyzing: {url} → {word_count} words")
    avg_word_count = total_words / len(competitor_urls)
    return {
        "total_competitors": len(competitor_urls),
        "avg_word_count": avg_word_count,
        "total_words": total_words
    }


# ============================================================
# COMPLETE DATA EXAMPLE
# ============================================================

print("=" * 60)
print("COMPLETE DATA EXAMPLE: analyze_competitors Function")
print("=" * 60)
print()


competitor_urls = [
    "https://competitor1.com/shilajit",
    "https://competitor2.com/shilajit",
    "https://competitor3.com/shilajit",
    "https://competitor4.com/shilajit",
    "https://competitor5.com/shilajit"
]

print("📊 INPUT DATA:")
print(f"Competitor URLs: {competitor_urls}")
print(f"Number of competitors: {len(competitor_urls)}")
print()


print("🔄 PROCESSING:")
insights = analyze_competitors(competitor_urls)
print()

print("📈 RESULTS:")
print(f"Total competitors analyzed: {insights['total_competitors']}")
print(f"Total words across all articles: {insights['total_words']}")
print(f"Average word count: {insights['avg_word_count']:.2f} words")
print()

print("🔍 ACCESSING SPECIFIC VALUES:")
print(f"Average word count (direct access): {insights['avg_word_count']}")
print(f"Total competitors (direct access): {insights['total_competitors']}")
print()

print("💡 USING THE INSIGHTS:")
if insights['avg_word_count'] > 1900:
    print("✅ Competitors write long articles (>1900 words)")
    print("   Recommendation: Write articles with 2000+ words")
else:
    print("⚠️  Competitors write shorter articles (<1900 words)")
    print("   Recommendation: Write articles with 1800-2000 words")

print()
print("=" * 60)
print("EXAMPLE COMPLETE!")
print("=" * 60)