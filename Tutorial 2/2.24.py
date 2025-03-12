"""Finding the mode of list of numbers(A number that appears most often is the
 mode.)"""

from collections import Counter

def find_mode(numbers):
    freq = Counter(numbers)
    max_count = max(freq.values())
    mode = [num for num, count in freq.items() if count == max_count]
    return mode

n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
print(f"\nThe mode is: {find_mode(numbers)}")
