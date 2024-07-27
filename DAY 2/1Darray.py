numbers = [15, 22, 8, 19, 30, 5]
if not numbers:
    print("The array is empty, so the range cannot be determined.")
else:
    max_value = max(numbers)
    min_value = min(numbers)
    range_value = max_value - min_value
    print(f"Range: {range_value}")
