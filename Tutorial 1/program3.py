def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

num = int(input("Enter a number: "))
print(check_even_odd(num))
