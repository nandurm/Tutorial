#Write a program to remove all occurrence of a substring from a string

s= input("Enter the string")
sub= input("Enter the substring ")

if sub in s:
    s = s.replace(sub, "")
    print(s)