s = input("Enter a comma-separated sequence of words: ")
words = s.split(',')
words = [word.strip() for word in words]
sorted_words = sorted(words)
output_string = ','.join(sorted_words)
print(output_string)
