from collections import Counter

def get_top_keywords(text, n=5):
    words = text.split()
    freq = Counter(words)
    return freq.most_common(n)