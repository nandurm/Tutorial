def OoE(num):
    if num==0:
        print(f"{num} is zero.")
    elif num%2==0:
        print(f"{num} is even.")
    else:
          print(f"{num} is odd.")

num=int(input("Enter the number: "))
check=OoE(num)