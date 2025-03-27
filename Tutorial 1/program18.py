def is_armstrong_number(num):
    power = len(str(num))
    return sum(int(digit) ** power for digit in str(num)) == num

num = int(input("Enter a number: "))
print(is_armstrong_number(num))
