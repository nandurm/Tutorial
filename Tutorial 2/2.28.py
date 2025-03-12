"""Write a Python program to read a list of numbers and sort the list in a non
decreasing order without using any built in functions. Separate function should
 be written to sort the list wherein the name of the list is passed as the parameter."""

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

bubble_sort(numbers)

print(f"\nSorted list in non-decreasing order: {numbers}")
