for num in range(100, 1001):
    sum_of_digits = 0
    n = num
    
    while n > 0:
        sum_of_digits += n % 10
        n //= 10

    if sum_of_digits % 9 == 0:
        print(num, end=" ")
