def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_krishnamurthy_number(num):
    original_num = num
    sum_factorial_digits = 0
    
    while num > 0:
        digit = num % 10
        sum_factorial_digits += factorial(digit)
        num //= 10
    
    return sum_factorial_digits == original_num
num = 145
if is_krishnamurthy_number(num):
    print(f"{num} is a Krishnamurthy number.")
else:
    print(f"{num} is not a Krishnamurthy number.")
