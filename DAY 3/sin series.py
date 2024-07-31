import math
def sine_series(x, n):
    sine_value = 0
    s = 1 
    for i in range(n):
        term = s * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        sine_value += term
        s *= -1 
    return sine_value
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms n: "))
if n > 0:
    result = sine_series(x, n)
    print(f"The sine of {x} using {n} terms is: {result}")
else:
    print("Please enter a positive integer for n.")
