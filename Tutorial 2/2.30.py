""" Remove duplicate elements from a list."""

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

print(f"\nList after removing duplicates: {remove_duplicates(numbers)}")
