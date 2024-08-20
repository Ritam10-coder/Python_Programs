s=str(input("Enter the String:"))
s1=s[::-1]
if s == s1:
    print(f'The string "{s}" is a palindrome.')
else:
    print(f'The string "{s}" is not a palindrome.')
