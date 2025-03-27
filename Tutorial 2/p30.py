# Program to completely remove duplicate elements without keeping any copy

def completely_remove_duplicates(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    return [num for num in frequency if frequency[num] == 1]

numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
print("List after completely removing duplicates:", completely_remove_duplicates(numbers))
