"""Consider a list consisting of integers, floating point numbers and strings.
 Separate them into different lists depending on the data"""

def separate_data_types(lst):
    integers = [x for x in lst if isinstance(x, int) and not isinstance(x, bool)]
    floats = [x for x in lst if isinstance(x, float)]
    strings = [x for x in lst if isinstance(x, str)]
    return integers, floats, strings

n = int(input("Enter the number of elements: "))
data = [eval(input(f"Enter element {i+1}: ")) for i in range(n)]

integers, floats, strings = separate_data_types(data)

print(f"\nIntegers: {integers}")
print(f"Floats: {floats}")
print(f"Strings: {strings}")
