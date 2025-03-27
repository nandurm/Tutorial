# Remove duplicate elements from a list.

def remove_duplicates(numbers):
    return list(set(numbers))

numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
print("List after removing duplicates:", remove_duplicates(numbers))

