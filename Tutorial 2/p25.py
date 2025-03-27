# Consider a list consisting of integers, floating point numbers and strings.
# Separate them into different lists depending on the data

def separate_data(data):
    integers = []
    floats = []
    strings = []
    for item in data:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, float):
            floats.append(item)
        else:
            strings.append(item)
    return integers, floats, strings

data = [eval(x) for x in input("Enter integers, floats, and strings separated by spaces: ").split()]
integers, floats, strings = separate_data(data)
print(f"Integers: {integers}, Floats: {floats}, Strings: {strings}")

