def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    
    return sum


num = int(input("Enter the number:"))
print(f"Sum of digits of {num} is:", sum_of_digits(num))

