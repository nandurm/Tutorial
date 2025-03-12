"""Write a Python program to check the validity of a password given by the user
11. The Password should satisfy the following criteria:
1. Contains at least one letter between a and z
2. Contains at least one number between 0 and 9
3. Contains at least one letter between A and Z
4. Contains at least one special character from $, #, @
Minimum length of password: 6"""

s=input("Enter the passsword ")
hasupper=False
haslower=False
hasdigit=False
hasspecial=False
specialChar="$@#"

if(len(s)>=6):
    for i in s:
        if i.islower():
            haslower=True
        elif i.isupper():
              hasupper=True
        elif i.isdigit():
              hasdigit=True
        elif i in specialChar:
            hasspecial=True

    if hasupper and haslower and hasdigit and hasspecial:
         print(" Pasword is vlaid")
    else:
         print("Invalid password")

else:
    print("invalid password")                        
