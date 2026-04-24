n=int(input("Enter the size of list : "))
l=[ ]
sum=0
for i in range (n):
    a=int(input("Enter the number :"))
    l.append(a)
ele_search=int(input("Enter the element to be searched :"))   
if ele_search in l:
    print(ele_search,"exists in list")
else:
    print(ele_search,"doesn't exist in list")
    