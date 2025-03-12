"""Write a program to do basic set operations"""

def set_operations(set1, set2):
    union_set = set1 | set2
    intersection_set = set1 & set2
    difference_set1 = set1 - set2
    difference_set2 = set2 - set1
    symmetric_difference_set = set1 ^ set2
    return union_set, intersection_set, difference_set1, difference_set2, symmetric_difference_set

set1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))

union_set, intersection_set, difference_set1, difference_set2, symmetric_difference_set = set_operations(set1, set2)

print(f"\nUnion: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference (Set1 - Set2): {difference_set1}")
print(f"Difference (Set2 - Set1): {difference_set2}")
print(f"Symmetric Difference: {symmetric_difference_set}")
