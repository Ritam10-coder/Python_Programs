def print_pattern():
    n = 4  
    pattern = [[0]*n for i in range(n)]
    num = 1
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                pattern[i][j] = num
                num += 1
        else:
            for j in range(n-1, -1, -1):
                pattern[i][j] = num
                num += 1
    pattern[1][3] = 5
    pattern[2][0] = 11
    pattern[2][1] = 16
    pattern[2][2] = 15
    pattern[2][3] = 6
    pattern[3][0] = 10
    pattern[3][1] = 9
    pattern[3][2] = 8
    pattern[3][3] = 7
    for row in pattern:
        for element in row:
            print(element, end=' ')
        print()
print_pattern()
