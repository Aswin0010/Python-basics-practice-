n=int(input("Enter the size of list : "))
l=[ ]
l2=[]
for i in range (n):
    a=int(input("Enter the number :"))
    l.append(a)
for j in range (len(l)):
    count=0
    if l[j] in l2:
        continue
    for k in range (len(l)):
            if l[j]==l[k]:
                count+=1
    l2.append(l[j])
    print("The frequency of",l[j],"is ",count)       