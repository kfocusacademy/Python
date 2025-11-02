import re

def remove_urls(text):
    return re.sub(r'https?://\S+|www\.\S+', '', text)

def to_lowercase(text):
    return text.lower()

def remove_non_alpha(text):
    return re.sub(r'[^a-zA-Z\s]', '', text)