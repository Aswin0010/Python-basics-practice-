n=int(input("Enter the size of list : "))
l=[ ]
for i in range (n):
    a=int(input("Enter the number :"))
    l.append(a)
max=l[0]   
for j in l:
    if max<j:
        max=j
    
print("maximum number :",max)    