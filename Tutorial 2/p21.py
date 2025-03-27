# Program to read a string and remove the given words from the string

def remove_words(s, words):
    for word in words:
        s = s.replace(word, '')
    return s

input_string = input("Enter a string: ")
words_to_remove = input("Enter words to remove (separated by commas): ").split(',')
print(remove_words(input_string, words_to_remove))
