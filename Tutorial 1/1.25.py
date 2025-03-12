def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

x = int(input("Enter the base (X): "))
y = int(input("Enter the exponent (Y): "))

print(f"{x}^{y} = {power(x, y)}")
