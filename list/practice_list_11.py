n=int(input("Enter the size of list : "))
l=[ ]
for i in range (n):
    a=int(input("Enter the number :"))
    l.append(a)
search_n=int(input("Enter the number to be searched: "))
index=0
for j in range (len(l)):
    if l[j]==search_n:
        index=j
        print("The index of first occurance of",search_n,"is",index)
        break
else:
    print("The number is not present in list")