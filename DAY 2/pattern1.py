def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        for k in range(2, i + 1):
            print(k, end=' ')
        print()
print_pattern(4)
