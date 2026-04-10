n=int(input("Enter the size of list : "))
l=[ ]
for i in range (n):
    a=input("Enter the number :")
    l.append(a)
start=0
end=n-1
while start<end:
    l[start],l[end]=l[end],l[start]
    start+=1
    end-=1
print("Reversed list :"l)    