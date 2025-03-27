# Write a Python program to print n’th Fibonacci number using recursion.

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter n: "))
print(fibonacci_recursive(n))
