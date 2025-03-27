# Write Python script for converting decimal number into Binary number.

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

decimal_number = int(input("Enter a decimal number: "))
print(decimal_to_binary(decimal_number))
