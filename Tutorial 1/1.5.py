from math import*

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
        return f"Two real and distinct roots: {root1:.2f}, {root2:.2f}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One real and repeated root: {root:.2f}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = sqrt(abs(discriminant)) / (2 * a)
        return f"Complex roots: {real_part:.2f} ± {imaginary_part:.2f}i"

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Not a quadratic equation (a should not be zero).")
else:
    print(find_roots(a, b, c))
