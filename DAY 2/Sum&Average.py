def calculate_sum_and_average(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return total_sum, average
def main():
    numbers = [10, 20, 30, 40, 50,70]
    total_sum, average = calculate_sum_and_average(numbers)
    print(f"Sum: {total_sum}")
    print(f"Average: {average:.2f}")
if __name__ == "__main__":
    main()
