"""Write a Python program to find the value for sin(x) up to n terms using the
 series
   sin(x)=1-x^3/3!+x^5/5!..... ( sin(x) = ((-1)^n/(2n+1)!)x^(2n+1) )"""


import math

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def sin_series(x, n_terms):
    sine_value = 0
    
    for n in range(n_terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        sine_value += term

    return sine_value

x_degrees = float(input("Enter the value of x in degrees: "))
n_terms = int(input("Enter the number of terms: "))

x_radians = math.radians(x_degrees)

result = sin_series(x_radians, n_terms)

print(f"sin({x_degrees}) ≈ {result}")
