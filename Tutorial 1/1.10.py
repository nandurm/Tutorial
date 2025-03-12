def sum_of_evens(n):
    total = 0  
    
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))  
        if num % 2 == 0: 
            total += num  
    
    return total 

N = int(input("Enter how many numbers: "))

print(f"Sum of even numbers: {sum_of_evens(N)}")
