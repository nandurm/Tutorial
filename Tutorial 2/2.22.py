""" Program to read a string and remove the given words from the string"""

def remove_words(text, words_to_remove):
    words = text.split()  
    filtered_words = [word for word in words if word not in words_to_remove]
    return " ".join(filtered_words) 

text = input("Enter a string: ")

words_to_remove = input("Enter words to remove (separated by spaces): ").split()

new_text = remove_words(text, words_to_remove)
print("\nString after removing given words:")
print(new_text)
