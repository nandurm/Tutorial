""" Write a program to replace all the spaces in the input string with * or if no
spaces found, put $ at the start and end of the string"""

s=input("Enter the string : ")
for i in s:
    if i==" ":
        s=s.replace(" ","*")

s=s+'$'

print(s)