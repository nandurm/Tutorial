""" Write a menu driven program to implement the following
 i)check even or odd
 ii)check number is positive negative or zero
 iii) generate factors of a number"""

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

def check_number_type(num):
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print(f"{num} is Zero")

def generate_factors(num):
    print(f"Factors of {num}: ", end="")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()

while True:
    print("\nMenu:")
    print("1. Check Even or Odd")
    print("2. Check if Number is Positive, Negative, or Zero")
    print("3. Generate Factors of a Number")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        num = int(input("Enter a number: "))
        check_even_odd(num)
    elif choice == 2:
        num = int(input("Enter a number: "))
        check_number_type(num)
    elif choice == 3:
        num = int(input("Enter a number: "))
        generate_factors(num)
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a valid option (1-4).")
