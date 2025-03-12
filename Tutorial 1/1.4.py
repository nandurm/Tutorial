def Compare(n1,n2):
    if n1>n2:
        print(f"{n1} is the largest")
        print(f"{n2} is the smallest")
    elif n1==n2:
        print(f"{n1} & {n2} are equal")
    else:
        print(f"{n2} is the largest")
        print(f"{n1} is the smallest")

n1=int(input("Enter the n1: "))
n2=int(input("Enter the n2: "))
Compare(n1,n2)