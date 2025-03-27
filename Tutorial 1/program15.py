def prime_numbers_below_1000():
    primes = []
    for num in range(2, 1000):
        if is_prime(num):
            primes.append(num)
    return primes

print(prime_numbers_below_1000())
