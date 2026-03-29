def calculate_ratio(number, base=100):
    if number == 0:
        raise ValueError("Cannot calculate ratio for zero")
    return base / number


def average_ratios(numbers):
    if not isinstance(numbers, list) or len(numbers) == 0:
        raise ValueError("Input must be a non-empty list of numbers")

    ratios = []
    for number in numbers:
        try:
            ratios.append(calculate_ratio(number))
        except ValueError as error:
            print(f"Skipping invalid value {number}: {error}")

    if not ratios:
        raise ValueError("No valid numbers available to calculate an average ratio")

    return sum(ratios) / len(ratios)


if __name__ == "__main__":
    values = [10, 5, 0]
    result = average_ratios(values)
    print(result)
