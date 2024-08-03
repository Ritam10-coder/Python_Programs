def print_pattern():
    n = 3
    total_elements = n * n
    spiral_order = []
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    while num <= total_elements:
        for i in range(left, right + 1):
            spiral_order.append(num)
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            spiral_order.append(num)
            num += 1
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral_order.append(num)
                num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral_order.append(num)
                num += 1
            left += 1

    index = 0
    for i in range(n):
        for j in range(n):
            print(spiral_order[index], end=" ")
            index += 1
        print()

print_pattern()
