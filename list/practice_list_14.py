n=int(input("Enter the size of list : "))
l=[ ]
print("Enter the elements of l :")
for i in range (n):
    l.append(int(input("Enter the number :")))
for j in range (0,len(l)//2):
    if l[j]!=l[len(l)-j-1]:
        print(l,"is not palindrome")
        break
else:
    print(l,"is palindrome")    
    