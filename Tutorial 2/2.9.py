#Write a Program to reverse the first and second half of a string separately

s=input("Enter the string : ")

n=len(s)
mid=n//2

for i in range(mid-1,-1,-1):
    print(s[i], end="")
for i in range(n-1,mid-1,-1):
    print(s[i], end="")