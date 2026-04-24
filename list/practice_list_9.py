n=int(input("Enter the size of list : "))
l=[ ]
sum=0
for i in range (n):
    a=int(input("Enter the number :"))
    l.append(a)
for j in range(len(l)):
    l[j]=l[j]**2
print(l)    