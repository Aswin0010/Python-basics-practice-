n=int(input("Enter the size of list : "))
l=[ ]
odd=0
even=0
for i in range (n):
    a=int(input("Enter the number :"))
    l.append(a)
for j in l:
    if j%2==0:
        even+=1
    else:
        odd+=1
print("odd number:",odd)
print("even number:",even) 