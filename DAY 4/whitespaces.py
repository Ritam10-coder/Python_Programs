def process_words():
    input_string = input("Enter a sequence of whitespace-separated words: ")
    words = input_string.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    output_string = ' '.join(sorted_words)
    print(output_string)
process_words()
