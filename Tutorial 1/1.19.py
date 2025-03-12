n = int(input("Enter the number of elements: "))

even_count = 0
odd_count = 0

for _ in range(n):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
