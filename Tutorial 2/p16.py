# Write a Python program to find the value for sin(x) up to n terms using the
# series sin(x)=1-x^3/3!+x^5/5!..... ( sin(x) = ((-1)^n/(2n+1)!)x^(2n+1) )

def sin_x(x, n):
    sine = 0
    for i in range(n):
        sign = (-1) ** i
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sine += sign * term
    return sine

x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))
print(sin_x(x, n))
