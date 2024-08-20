s = str(input("Enter the string:"))
vowels=['a','e','i','o','u','A','E','I','O','U']
res=""
for i in range(len(s)):
    if s[i] not in vowels:
        res=res+s[i]
print(res)        