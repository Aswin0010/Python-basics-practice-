n=int(input("Enter the size of list : "))
l=[ ]
print("Enter the elements of l :")
for i in range (n):
    l.append(int(input("Enter the number :")))
for k in range (len(l)):
    if l[k]==0:
        for j in range (k+1,len(l)):
            if l[j]!=0:
                l[k]=l[j]
                l[j]=0
                break
print(l)