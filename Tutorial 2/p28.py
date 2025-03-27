# Write a program to do basic set operations

def set_operations(set1, set2):
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    difference = set1.difference(set2)
    return union, intersection, difference

set1 = set(map(int, input("Enter elements of first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by spaces: ").split()))
union, intersection, difference = set_operations(set1, set2)
print(f"Union: {union}, Intersection: {intersection}, Difference: {difference}")
