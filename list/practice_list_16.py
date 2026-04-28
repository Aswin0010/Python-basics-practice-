n=int(input("Enter the size of list : "))
l=[ ]
l2=[ ]
print("Enter the elements of l :")
for j in range (n):
    l.append(int(input("Enter the number :")))
l.sort()    
for i in range (n):
    if (i+1)!=l[i]:
       print((i+1),"is missing")
       break
else:
    print("no number is missing")       