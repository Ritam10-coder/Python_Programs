def pattern(num):
    for i in range(1, num + 1):
        if i % 2 == 1:
            start = (i - 1) * 2 + 1
            end = start + 2
            for j in range(start, end):
                print(j, end=" ")
        else:
            start = i * 2
            for j in range(start, start - 2, -1):
                print(j, end=" ")
        print()  
num = 2
pattern(num)

