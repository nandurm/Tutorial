# Program to read list of numbers and find the median

def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    return numbers[mid]

numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(find_median(numbers))
