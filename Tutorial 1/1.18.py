def is_armstrong(num):
    temp = num
    digits = 0
    sum_of_powers = 0
    
    n = num
    while n > 0:
        n //= 10
        digits += 1

    n = temp
    while n > 0:
        digit = n % 10
        sum_of_powers += digit ** digits
        n //= 10

    return temp == sum_of_powers

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")
