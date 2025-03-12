"""Write Python script for converting decimal number into Binary number."""




def decimal_to_binary(n):
    binary = ""
    
    if n == 0:
        return "0"
    
    while n > 0:
        binary = str(n % 2) + binary  
        n = n // 2 
        print(binary)
    
    return binary


decimal = int(input("Enter a decimal number: "))

print(f"Binary representation: {decimal_to_binary(decimal)}")