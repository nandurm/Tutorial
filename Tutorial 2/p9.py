#Write a Program to reverse the first and second half of a string separately

def reverse_half(s):
    mid = len(s) // 2
    first_half = s[:mid][::-1]
    second_half = s[mid:][::-1]
    return first_half + second_half

input_string = input("Enter a string: ")
print(reverse_half(input_string))
