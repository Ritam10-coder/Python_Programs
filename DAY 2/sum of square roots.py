import math
def sum_of_square_roots(a, b, c):
    sum_sqrt = math.sqrt(a) + math.sqrt(b) + math.sqrt(c)
    return sum_sqrt
a = 9
b = 16
c = 25
result = sum_of_square_roots(a, b, c)
print("Sum of square roots:", result)
