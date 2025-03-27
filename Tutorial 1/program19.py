def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return even_count, odd_count

n = int(input("How many numbers will you enter? "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
even_count, odd_count = count_even_odd(numbers)
print(f"Even Count: {even_count}, Odd Count: {odd_count}")
