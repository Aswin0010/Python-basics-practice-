n=int(input("Enter the size of list : "))
l=[ ]
sum=0
for i in range (n):
    a=int(input("Enter the number :"))
    l.append(a)
for j in l:
    sum=sum+j
print("sum of elements:",sum)