#Write a python script for palindrome checking without reversing the string

def is_palindrome(s):
    n=len(s)
    left=0
    for i in range(0, int(n/2)):
       if s[i] != s[n-i-1]:
           return False
    return True


s= input("Enter the string : ")
if is_palindrome(s):
    print("The string is paliendrome")
else :
    print("The string is not palidrome")