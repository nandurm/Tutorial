# Write a program to remove characters at odd index positions from a string

def remove_odd_index(s):
    return ''.join(s[i] for i in range(len(s)) if i % 2 == 0)

input_string = input("Enter a string: ")
print(remove_odd_index(input_string))
