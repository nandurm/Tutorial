# Write Python script for converting decimal number into Binary number.

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

decimal_number = int(input("Enter a decimal number: "))
print(decimal_to_binary(decimal_number))


# 12. Convert binary number into decimal number.
def binary_to_decimal(b):
    return int(b, 2)

binary_number = input("Enter a binary number: ")
print(binary_to_decimal(binary_number))
