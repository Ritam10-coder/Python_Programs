def count(sentence):
    letters = 0
    digits = 0
    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return letters, digits
s = input("Enter a sentence: ")
letters_count, digits_count = count(s)
print(f"Number of letters: {letters_count}")
print(f"Number of digits: {digits_count}")
 