import cmath
def solve_quadratic_eqn_(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return root1, root2
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of a:"))
print("The solution of quadratic equation :",solve_quadratic_eqn_(a, b, c))