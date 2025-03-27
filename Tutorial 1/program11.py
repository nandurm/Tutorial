def sum_of_cubes_of_evens(n):
    return sum(i**3 for i in range(2, n + 1, 2))

n = int(input("Enter a positive integer: "))
print(sum_of_cubes_of_evens(n))
