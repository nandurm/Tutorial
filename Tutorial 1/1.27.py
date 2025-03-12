import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Two real and distinct roots: {root1:.2f}, {root2:.2f}")

elif discriminant == 0:
    root = -b / (2 * a)
    print(f"One real and equal root: {root:.2f}")

else:
    real_part = -b / (2 * a)
    imag_part = math.sqrt(abs(discriminant)) / (2 * a)
    print(f"Two complex roots: {real_part:.2f} ± {imag_part:.2f}i")
