""" Program to find the sum of all even numbers in a group of n numbers entered
 by the user"""

n = int(input("Enter the number of elements: "))

even_sum = 0

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_sum += num

# Display the result
print(f"\nSum of all even numbers: {even_sum}")
