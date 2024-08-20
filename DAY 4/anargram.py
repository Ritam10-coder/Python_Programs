s = str(input("Enter the string:"))
s1 = str(input("Enter the string:"))
if sorted(s)==sorted(s1):
    print(f'The strings "{s}" and "{s1}" are anagrams.')
else:
    print(f'The strings "{s}" and "{s1}" are not anagrams.')