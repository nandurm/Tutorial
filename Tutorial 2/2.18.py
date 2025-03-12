""" Write a Python program to print the factorial of a number using recursion"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Get user input
num = int(input("Enter a number: "))

# Validate input
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")
