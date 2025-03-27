def compare_numbers(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is less than {b}"
    else:
        return "Both numbers are equal"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(compare_numbers(num1, num2))
