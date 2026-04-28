n=int(input("Enter the size of list : "))
l=[ ]
l2=[ ]
print("Enter the elements of l :")
for i in range (n):
    l.append(int(input("Enter the number :")))
a=int(input("Enter the position to rotate :")) 
a=a%n
for j in range (len(l)):
    if j<a:
       l2.append(l[len(l)-a+j])
    else:
        l2.append(l[j-a])   
print(l2)    