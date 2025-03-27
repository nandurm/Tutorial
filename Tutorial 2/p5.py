# Write a program to slice the string into two separate strings; one with all the
# characters in the odd indices and one with all characters in even indices.

def slice_string(s):
    odd_indices = ''.join(s[i] for i in range(len(s)) if i % 2 != 0)
    even_indices = ''.join(s[i] for i in range(len(s)) if i % 2 == 0)
    return even_indices, odd_indices

input_string = input("Enter a string: ")
even, odd = slice_string(input_string)
print(f"Even indices: {even}, Odd indices: {odd}")
