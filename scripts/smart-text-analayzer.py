from collections import Counter
import re

# Sample text
text = "This is a sample text. This text contains sample words."

# Convert to lowercase and remove non-alphabetic characters
words = re.findall(r'\b[a-z]+\b', text.lower())

# Create a Counter object from the list of words
word_counts = Counter(words)


# Calculate the total word count by summing the values in the Counter
total_word_count = sum(word_counts.values())

# Calculate the total length of all words
total_length = sum(len(word) for word in words)

total_words = len(words)


if total_words > 0:
    average_word_length = total_length / total_words
else:
    average_word_length = 0

# Find the longest word(s)
if words:
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
else:
    longest_words = []


# Print the Counter object to see all word frequencies
print(f"\nFrequency of 'words': {word_counts}")

print(f"Total word count: {total_word_count}")

print(f"Average word length: {average_word_length:.2f}")

print(f"Longest words: {longest_words}")
