# Program to find the sum of all even numbers in a group of n numbers entered by the user

def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

n = int(input("How many numbers will you enter? "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
print(sum_of_even_numbers(numbers))
