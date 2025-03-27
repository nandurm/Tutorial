# Finding the mode of list of numbers(A number that appears most often is the mode.)

def find_mode(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    mode = max(frequency, key=frequency.get)
    return mode

numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
print("Mode:", find_mode(numbers))
