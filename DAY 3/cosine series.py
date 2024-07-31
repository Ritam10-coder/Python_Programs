import math
def cosine_series(x, n):
    cosine_value = 0
    sign = 1 
    for i in range(n):
        term = sign * (x ** (2 * i)) / math.factorial(2 * i)
        cosine_value += term
        sign *= -1 
    return cosine_value
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms n: "))

if n > 0:
    result = cosine_series(x, n)
    print(f"The cosine of {x} using {n} terms is: {result}")
else:
    print("Please enter a positive integer for n.")
