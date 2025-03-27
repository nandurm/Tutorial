def prime_factors(n):
    factor = 2
    while n > 1:
        if n % factor == 0:
            print(factor, end=" ")
            n //= factor
        else:
            factor += 1

num = int(input("Enter a number: "))
print("Prime factors:", end=" ")
prime_factors(num)
