n=int(input("Enter the size of list : "))
l=[ ]
sum=0
for i in range (n):
    a=int(input("Enter the number :"))
    l.append(a)
ele_rem=int(input("Enter the element to be removed :"))   
if ele_rem in l:
    l.remove(ele_rem)
print(l)    