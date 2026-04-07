s=input("Enter the string s : ")
l=len(s)
for i in range (0 ,l//2):
    if(s[i]!=s[l-i-1]):
        print(s,"is not palindrom")
        break
else:
    print(s,"is palindrom")    
        
