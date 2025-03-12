def remove_vowels(s):
    return "".join(char for char in s if char.lower() not in "aeiou")

input_string = "Hello, World!"
print("String after removing vowels:", remove_vowels(input_string))
