def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    
    result = 1
    for i in range(exponent):
        result += result 
    return result
print(power(2, 3))
