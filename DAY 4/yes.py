def extract_digit_words(input_string):
    words = input_string.split()
    digit_words = [word for word in words if word.isdigit()]
    return digit_words
input_string = input("Enter a sequence of words separated by whitespace: ")
result = extract_digit_words(input_string)
print(result)
