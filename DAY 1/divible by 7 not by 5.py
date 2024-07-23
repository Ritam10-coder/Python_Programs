start = 1000
end = 2000
found_number = None
for num in range(start, end + 1):

   if num % 7 == 0 and num % 5 != 0:
        found_number = num
        break  

if found_number is not None:
    print(f"A number between {start} and {end} that is divisible by 7 but not by 5 is: {found_number}")
else:
    print(f"No such number found between {start} and {end}.")

   
