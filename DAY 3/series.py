def series(num):
    sum = 0.0
    for i in range(1, num + 1):
        if i % 2 == 0:
            sum -= 1 / i 
        else:
            sum += 1 / i  
    return sum

num = int(input("Enter a positive integer : "))
if num > 0:
    result = series(num)
    print(f"The sum of the series up to {num} terms is: {result}")
else:
    print("Please enter a positive integer.")
