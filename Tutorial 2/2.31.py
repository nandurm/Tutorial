""" Program to completely remove duplicate elements without keeping any copy"""

from collections import Counter

def remove_all_duplicates(lst):
    freq = Counter(lst)
    return [x for x in lst if freq[x] == 1]

n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

print(f"\nList after completely removing duplicates: {remove_all_duplicates(numbers)}")
