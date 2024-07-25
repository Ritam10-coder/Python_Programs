def print_pattern(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()
print_pattern(4)
