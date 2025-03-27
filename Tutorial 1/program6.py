def is_right_triangle(a, b, c):
    return a**2 + b**2 == c**2

side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))
sides = sorted([side1, side2, side3])
print(is_right_triangle(sides[0], sides[1], sides[2]))
