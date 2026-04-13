n=int(input("Enter the size of list : "))
l=[ ]
for i in range (n):
    a=input("Enter the number :")
    l.append(a)
min=l[0]   
for j in l:
    if min>j:
        min=j
print("minimum number :",min)    