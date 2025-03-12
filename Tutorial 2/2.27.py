""" Write a Python program to read list of positive integers and separate the prime
 and composite numbers """

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def separate_prime_composite(lst):
    primes = [x for x in lst if is_prime(x)]
    composites = [x for x in lst if x > 1 and not is_prime(x)]
    return primes, composites

n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter positive integer {i+1}: ")) for i in range(n) if int(input(f"Enter positive integer {i+1}: ")) > 0]

primes, composites = separate_prime_composite(numbers)

print(f"\nPrime numbers: {primes}")
print(f"Composite numbers: {composites}")
