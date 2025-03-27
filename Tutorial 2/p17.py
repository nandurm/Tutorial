# Write a Python program to print the factorial of a number using recursion

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

num = int(input("Enter a number: "))
print(factorial_recursive(num))
