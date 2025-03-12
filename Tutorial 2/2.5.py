"""Write a program to slice the string into two separate strings; one with all the
characters in the odd indices and one with all characters in even indices.
"""


s= input("Enter the string : ")
list1=list(s)
odd=[ ]
even=[]
for i in range(len(list1)):
    if i%2==0:
        even.append(list1[i])
    else:
        odd.append(list1[i])

print(list1)
print("even elements = ",even)
print("odd elements = ",odd)