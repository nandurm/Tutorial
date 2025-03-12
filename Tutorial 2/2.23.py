"""Program to read list of numbers and find the median"""

def find_median(numbers):
    numbers.sort()  
    n = len(numbers)
    
    if n % 2 == 1:
        return numbers[n // 2]  
    else:
        mid1, mid2 = numbers[n // 2 - 1], numbers[n // 2]  
        return (mid1 + mid2) / 2  

n = int(input("Enter the number of elements: "))


numbers = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: ")) 
    numbers.append(num)


median = find_median(numbers)
print(f"\nThe median is: {median}")
