n=int(input("Enter the size of list : "))
l=[ ]
l2=[ ]
print("Enter the elements of l :")
for i in range (n):
    l.append(int(input("Enter the number :")))
l.sort()
for j in range(n):
    if l[j] in l2:
        continue 
    else:
        l2.append(l[j])    
print(l2)        