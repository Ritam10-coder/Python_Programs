from collections import Counter
import re
text = "India is my motherland. I love my country. Capital of India is New Delhi."
text = text.lower()
words = re.findall(r'\b\w+\b', text)
word_counts = Counter(words)
for word, count in word_counts.items():
    print(f'{word}: {count}')
