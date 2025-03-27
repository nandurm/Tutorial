def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

x = int(input("Enter base (X): "))
y = int(input("Enter exponent (Y): "))
print(power(x, y))
